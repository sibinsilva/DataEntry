from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
import openpyxl
import time

chromedriver_autoinstaller.install() 
driver = webdriver.Chrome()

# Replace 'form_url' with the URL of the form you want to fill
form_url = "http://127.0.0.1:5000/"
driver.get(form_url)

def read_excel_data(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(row)
    return data


samples = read_excel_data('./sample_data.xlsx')

# Fill the form
for item in samples:
    first_name_field = driver.find_element(By.NAME, 'firstName')
    first_name_field.send_keys(item[0])

    last_name_field = driver.find_element(By.NAME, 'lastName')
    last_name_field.send_keys(item[1])

    dob_field = driver.find_element(By.NAME, 'dob')
    dob_field.send_keys(item[2].strftime("%d/%m/%Y"))

    sex_field = driver.find_element(By.NAME, 'gender')
    sex_field.send_keys(item[3])  # Assuming Male is the option you want to select

    address1_field = driver.find_element(By.NAME, 'address1')
    address1_field.send_keys(item[4])

    address2_field = driver.find_element(By.NAME, 'address2')
    address2_field.send_keys('' if item[5] is None else item[5])

    address3_field = driver.find_element(By.NAME, 'address3')
    address3_field.send_keys('' if item[6] is None else item[6])

    address4_field = driver.find_element(By.NAME, 'address4')
    address4_field.send_keys('' if item[7] is None else item[7])

    postcode_field = driver.find_element(By.NAME, 'postcode')
    postcode_field.send_keys(item[8])

    phone_field = driver.find_element(By.NAME, 'phone')
    phone_field.send_keys(item[9])

    email_field = driver.find_element(By.NAME, 'email')
    email_field.send_keys(item[10].replace(" ", ""))

    # If there's a submit button, click it
    try:
        driver.find_element(By.XPATH, '//input[@type="submit"]').click()
    except:
        print("No submit button found. Please submit the form manually.")
    
    # Check for alert and click OK
    try:
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert.accept()
        print("Alert detected and accepted")
        time.sleep(2)
    except:
        print("No alert detected")


# Close the browser
driver.quit()
