from getUserdataFromCampus import get_all_users_by_campus, read_user_data_from_csv, process_user, append_to_csv
from crwaling import login_and_process_users
from levelMaker import levelMaker
from supplement import parseAssignmentAndExam
from csvMerge import merge_csvfile
from searchGroup import parse_generation
from supplement_method import getKeyCsv
import pandas as pd

# calling users of given campus with campus id. the records will be stored in csv
get_all_users_by_campus()

# given user_id from get_all_users_by_campus, check evaluation of giving, receiving during exam.
user_ids = read_user_data_from_csv("./user_data_campus_1.csv", 0)
for user_id in user_ids:
    result_correct = process_user(user_id)
    append_to_csv(result_correct, "./user_feedback_data_campus_1.csv")
feedback = "./user_feedback_data_campus_1.csv"
    
user_name_lists = read_user_data_from_csv("./user_data_campus_1.csv", 2)
id = "junoh"
pw = "Hs06b2c28!!!"

csv_list = []

# crawling pass of exam, scores of assignments and exams. 
Pass = login_and_process_users(id, pw, user_name_lists)

# parse pass of exam, the number of groups assigments, highest personal assignment, score of final exam.
newUser_data = parseAssignmentAndExam()

# parse scores of all of assignments and exams to calculate level of users
levelMaker()
# drop almost attributes except ld, login(user name), create time, 
key = getKeyCsv("./user_data_campus_1.csv")
# classfy create time into generation
generationKey = parse_generation(key)
csv_list.append(newUser_data)
csv_list.append(Pass)
csv_list.append(feedback)
csv_list.append(generationKey)

merged_df = pd.merge(merged_df, df, on=key, how='inner')

