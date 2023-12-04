from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time
import csv

def login_and_process_users(id, pw, name_list):
    chrome_options = Options()
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Set timeouts (optional)
    driver.set_page_load_timeout(30)  # Page load timeout
    driver.implicitly_wait(10)        # Implicit wait
    
    
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.set_window_size(1200, 800)
    driver.get('https://auth.42.fr/auth/realms/students-42/protocol/openid-connect/auth?client_id=intra&redirect_uri=https%3A%2F%2Fprofile.intra.42.fr%2Fusers%2Fauth%2Fkeycloak_student%2Fcallback&response_type=code&state=da12ad7d8db1c8d93ca8c311270b6fd89b77f1b020ed0161')

    # Log in
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, 'username'))).send_keys(id)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys(pw)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, 'login'))).click()

    # Wait for login to complete
    time.sleep(5)
    dic_name_level = {}
    # get the result of pass exam.
    with open("pass.csv", 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["login", "Pass"])
        for name in name_list:
            # Search for the user
            try:
                
                search_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, 'query')))
                search_input.click()  # Explicitly click on the input field

                # Clear the input field using backspace
                search_input.send_keys(Keys.COMMAND + "a")
                search_input.send_keys(Keys.BACK_SPACE)

                search_input.send_keys(name)  # Enter the new name
                WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'tt-menu')))


                # Navigate to user's profile
                name_link = f'a[href="https://profile.intra.42.fr/users/{name}"]'
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, name_link))).click()

                try:
                # Try to select 'C Piscine' from dropdown
                    cursus_dropdown = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'select.cursus-user-select')))
                    Select(cursus_dropdown).select_by_value('c-piscine')
                    dic_name_level[name] = 1
                    
                except TimeoutException:
                # If the dropdown is not found, just continue
                    dic_name_level[name] = 0
                    pass
                print(f'{name} = {dic_name_level[name]}')
                xpath = "/html/body/div[4]/div[2]/div/div[3]/div[2]/div/div[2]/div[1]/div"
                collected_item = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath))).text
                print(f"Collected item for {name}: {collected_item}")
                with open('./newScore.txt', 'a') as file:
                    file.write("-----------------------------------------------------------------------\n")
                    file.write(name + "\n") 
                    file.write(collected_item + "\n")
                csv_writer.writerow([name, dic_name_level[name]])

                
                
            except TimeoutException as e:
                print(f"Timeout exception for {name}: {e}")
            except Exception as e:
                print(f"An error occurred for {name}: {e}")
    driver.quit()
    return "pass.csv"