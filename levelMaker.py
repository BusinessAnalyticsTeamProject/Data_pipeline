import csv

def levelMaker():
    file_path = './newScore.txt' # get scores from file.
    with open(file_path, 'r') as file:
        data = file.readlines()
    
    with open("newUser_data.csv", 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow("level")
            
        user_blocks = []
        current_block = []

        for line in data: # parse line per "-----"  
            if "-------" in line:
                if current_block:
                    user_blocks.append(current_block)
                    current_block = []
            else:
                current_block.append(line.strip())
        if current_block:
            user_blocks.append(current_block)
        for block in user_blocks:
            if block:
                c_piscine_c_score = 0
                exam_score = 0
                groupAssignmentScore = 0
                level = 0
                for i, line in enumerate(block[1:]):
                        # get scores of C, shell assignment
                    if line.startswith("C Piscine C ") or line.startswith("C Piscine Shell "):  #c piscine assignment collection
                       if block[i + 2].isdigit() and int(block[i + 2]) > 50:
                            c_piscine_c_score += int(block[i + 2])
                        # get scores of Exams
                    elif line.startswith("C Piscine Exam ") and block[i + 2].isdigit():
                        exam_score += int(block[i + 2])
                    elif line.startswith("C Piscine Final Exam ") and block[i + 2].isdigit():
                        # Final exam has much higher weight. Refelecting it with actual weights
                        exam_score += int(block[i + 2]) * (375 / 225)
                    elif (line.startswith("C Piscine Rush ") or line.startswith("C Piscine BSQ ")) and block[i + 2].isdigit() and int(block[i + 2]) > 80:
                        groupAssignmentScore += int(block[i + 2])
                        # Weighting assignments, exams scores
                level = c_piscine_c_score + exam_score * (225/100) + groupAssignmentScore * (150/100)
                level *= (8.41 / 1543) #scaling(8.41 means actual level of real one user, 1543 is the sum of scores of that person)
                csv_writer.writerow([round(level, 2)])
    return "level.csv"