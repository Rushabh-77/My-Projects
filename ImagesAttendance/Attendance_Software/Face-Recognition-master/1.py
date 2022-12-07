from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

import io
import os
import re
from google.cloud import vision
from PIL import Image
from PIL import ImageFile, ImageEnhance, ImageFilter
from io import BytesIO
import uuid
from bs4 import BeautifulSoup
# # from python3_anticaptcha import ImageToTextTask


# driver = webdriver.Chrome(executable_path='D:\\Idfy_projects\\wedax\\xlsx_file',chrome_options=options);

PATH = 'chromedriver.exe'
web = webdriver.Chrome(PATH)  # Or Chrome(), or Ie(), or Opera()
web.get('https://www.esic.in/EmployerSearch')




# drop_down_d.click()
# img_location = web.find_element_by_xpath('//*[@id="CaptchaImage"]')
# ImageEnhance.Contrast(img)
# with open('Logo.png', 'wb') as file:
#     file.write(web.find_element_by_xpath('//*[@id="CaptchaImage"]').screenshot_as_png)
def detect_text_gcv1(path, public_id, attempt_count):
    try:
        client = vision.ImageAnnotatorClient()
        with io.open(path, "rb") as image_file:
            content = image_file.read()

        image = vision.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations
        text = texts[0].description
        if text:
            return re.sub(r"\W+", "", text)
            
        else:
            return False
    except:
        pass
# web.save_screenshot(img_location)
# web.save_screenshot('ss.png')







captcha_img_response =  web.find_element_by_id("CaptchaImage")
# captcha_img_response.screenshot('foo.png')





if captcha_img_response:
    image_name = "CAPTCHA_image_" + str(uuid.uuid1()) + ".png"
    captcha_img_response.screenshot(image_name)
    img = Image.open(image_name)

    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    img.save(image_name)
    result_status = True
    response = image_name
    cap_text = detect_text_gcv1(response, '123', '1')
    print('************************************')
    print(cap_text)
    print('************************************')

    os.remove(image_name)


employer_state= "Maharashtra",
employer_district="Mumbai City",
employer_code="35000363090001099",
employer_name="Baldor Technologies"
if (employer_code or employer_name):
    if employer_code:
        e_code = web.find_element_by_xpath('//*[@id="txtemployercode"]')
        e_code.send_keys(employer_code)
    if employer_name:
        e_name = web.find_element_by_xpath('//*[@id="txtemployername"]')
        e_name.send_keys(employer_name)   
    drop_down_s = web.find_element_by_id('ddlstate')
select_state = Select(drop_down_s)
select_state.select_by_visible_text(employer_state)
time.sleep(1)
drop_down_d = web.find_element_by_id('ddldistrict')
select_dis = Select(drop_down_d)
select_dis.select_by_visible_text(employer_district)
captcha_field = web.find_element_by_xpath('//*[@id="CaptchaInputText"]')
captcha_field.send_keys(cap_text)
print(cap_text)
submit = web.find_element_by_xpath('//*[@id="SubmitId"]')
s = submit.click()
# print(s)
time.sleep(2)
scraped_response = web.page_source.encode('utf-8')

soup = BeautifulSoup(scraped_response, "html.parser")

div_CAPTCHA_error = soup.find(class_='Error')
employer_data = BeautifulSoup(str(soup.find_all(class_='odd')[0]),'html.parser')
           
employer_code = employer_data.find_all('td')[0]
print(employer_code.text.strip())
emp_code = web.find_element_by_xpath('//*[@id="myDataTable"]/tbody/tr/td[1]/a')
s = emp_code.click()
print(emp_code)
time.sleep(2)
xls_file = web.find_element_by_xpath('//*[@id="demo"]/a[2]')
x = xls_file.click()
# with open("emp_xlsx.xlsx", 'w+') as f:
#     f.write(x.content)
# xls = web.page_source.encode('utf-8')
# print(xls)
