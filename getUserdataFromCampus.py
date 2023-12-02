import requests
import json
import csv
import pandas as pd
import os

# 기존 코드에서 가져온 부분
UID = "u-s4t2ud-74766556a4e743fc75b26498d8f22e2c6444da37b87ddf898ea7fe883a3ddfd3"
SECRET = "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"
BASE_URL = "https://api.intra.42.fr"

auth = (UID, SECRET)
response = requests.post(f"{BASE_URL}/oauth/token", auth=auth, data={
    'grant_type': 'client_credentials',
    'client_id': UID,
    'client_secret': SECRET
})
response.raise_for_status()
token_data = response.json()
access_token = token_data["access_token"]

headers = {
    "Authorization": f"Bearer {access_token}"
}

params = {
    "page[size]": "100",
    "page[number]": "1"
    
}

def get_all_users_by_campus(campus_id=1, per_page=100):
    # Make API call to get user data for a specific campus with pagination
    page = 1
    all_user_data = []

    while True:
        endpoint = f"/v2/campus/{campus_id}/users"
        params = {'page': page, 'per_page': per_page}
        response = requests.get(f"{BASE_URL}{endpoint}", headers=headers, params=params)
        response.raise_for_status()
        user_data = response.json()

        if not user_data:
            break

        all_user_data.extend(user_data)
        page += 1

    # CSV file path for user data
    csv_file_path = f"./user_data_campus_{campus_id}.csv"

    # Extract fields from the first entry in user_data
    fields_to_include = []
    if all_user_data:
        # Check if the first entry is a dictionary
        if isinstance(all_user_data, dict):
            fields_to_include = list(all_user_data.keys())
        else:
            fields_to_include = list(all_user_data[0].keys())

    # Check if the file already exists, if not, create it and write the header
    if not os.path.isfile(csv_file_path):
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write the header with the selected fields
            writer.writerow(fields_to_include)

    # Append user data to CSV file with all fields
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if isinstance(all_user_data, dict):
            # If all_user_data is a dictionary, write its values directly
            writer.writerow(all_user_data.values())
        else:
            # If all_user_data is a list, iterate through its entries and write their values
            for user_entry in all_user_data:
                writer.writerow(user_entry.values())

    print(f"All users from campus {campus_id} data has been successfully written to {csv_file_path}")

def get_as_corrector(user_id, page_number):
    params["page[number]"] = str(page_number)
    endpoint = f"/v2/users/{user_id}/scale_teams/as_corrector"
    response = requests.get(f"{BASE_URL}{endpoint}", headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def get_as_corrected(user_id, page_number):
    params["page[number]"] = str(page_number)
    endpoint = f"/v2/users/{user_id}/scale_teams/as_corrected"
    response = requests.get(f"{BASE_URL}{endpoint}", headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def count_word_occurrences(json_data, word):
    return json_data.lower().count(word)

def process_user(user_id):
    # "/v2/users/{user_id}/scale_teams/as_corrector" 엔드포인트에 대한 요청
    response_corrector1 = get_as_corrector(user_id, 1)
    # "/v2/users/{user_id}/scale_teams/as_corrected" 엔드포인트에 대한 요청
    response_corrected1 = get_as_corrected(user_id, 1)
    # JSON 응답을 가져와서 단어 개수 세기
    corrector_count = count_word_occurrences(json.dumps(response_corrector1), "corrector")
    corrected_count = count_word_occurrences(json.dumps(response_corrected1), "correcteds")
    
    response_corrector2 = get_as_corrector(user_id, 2)
    response_corrected2 = get_as_corrected(user_id, 2)
    corrector_count += count_word_occurrences(json.dumps(response_corrector2), "corrector")
    corrected_count += count_word_occurrences(json.dumps(response_corrected2), "corrected")

    return {
        "id": user_id,
        "corrector": corrector_count,
        "corrected": corrected_count
   }

# CSV 파일 작성 함수
def append_to_csv(data, filename):
    with open(filename, "a", newline="") as csvfile:
        fieldnames = ["id", "corrector", "corrected"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # 각 사용자에 대한 처리
        # CSV 파일에 데이터 작성
        writer.writerow(data)
        print(f"{data['id']} is appended")

# 유저 리스트 받아오기
def read_user_data_from_csv(csv_file, column_number):
    df = pd.read_csv(csv_file)
    # 첫 번째 열의 데이터를 읽어옴 (헤더 제외)
    user_ids = df.iloc[:, column_number].tolist()
    return user_ids



get_all_users_by_campus()
user_ids = read_user_data_from_csv("./user_data_campus_1.csv", 0)
for user_id in user_ids:
    result_correct = process_user(user_id)
    append_to_csv(result_correct, "./user_feedback_data_campus_1.csv")