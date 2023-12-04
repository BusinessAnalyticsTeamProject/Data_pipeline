import csv

def parseAssignmentAndExam(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    
    with open("newUser_data.csv", 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["login", "Highest C Piscine", "Final exam score", "Number of group assignments"])
            
        user_blocks = []
        current_block = []

        for line in data:
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
                user_name = block[0]
                c_piscine_c_numbers = []
                final_exam_score = None
                groupAssignment = 0

                for i, line in enumerate(block[1:]):
                    if line.startswith("C Piscine C "):  #c piscine assignment collection
                        number_part = line.split()[3]
                        if number_part.isdigit():
                            c_piscine_c_numbers.append(int(number_part))
                    elif "C Piscine Final Exam" in line:
                        print(block[i + 2])
                        # Check if the next line contains the score
                        if i + 1 < len(block) and block[i + 2].isdigit():
                            final_exam_score = int(block[i + 2])
                    elif any(rush in line for rush in ["C Piscine Rush 00", "C Piscine Rush 01", "C Piscine Rush 02", "C Piscine BSQ"]):
                        groupAssignment += 1

                highest_c_piscine_c = max(c_piscine_c_numbers) if c_piscine_c_numbers else 0
                csv_writer.writerow([user_name, highest_c_piscine_c, final_exam_score if final_exam_score is not None else "N/A", groupAssignment])
    return "newUser_data.csv"