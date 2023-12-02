import os
import csv
import pandas as pd

def makeDirRightUnder(dir_name):

    dir_name = "./" + dir_name
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print(f"Directory {dir_name} created.")
    else:
        print(f"Directory {dir_name} already exists.")

def RecordName(name_list_2D):
    flattened_list = [name for sublist in name_list_2D for name in sublist]
    with open('./nameList_paris.txt', 'w') as file:
        for item in flattened_list:
            file.write(f"{item}\n")

def makeNameListFromCSV(csv_file_path):
    # CSV 파일에서 'login' 열의 데이터를 추출하여 리스트로 반환
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # 첫 번째 행(헤더) 건너뛰기
        names = [row[1] for row in reader]  # 'login' 열의 데이터 추출
    return names

def getKeyCsv(oringalCsv):
    df = pd.read_csv(oringalCsv)
    df = df[['id', 'login', 'created_at']]
    df.to_csv('key.csv', index=False)
    return "key.csv"
