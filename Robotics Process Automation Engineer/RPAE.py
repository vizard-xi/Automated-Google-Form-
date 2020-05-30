from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import getpass

def automation():
    #array of details for form filling
    details = ["Boakye Kelvin Prince", "kelvin.prince.336@gmail.com", "Ho Techinal University",
                 "EA-0326-5607", "0503877811", "Script Completed!!"]

    #email password
    email_password = getpass.getpass("Email Password: ")

    #chrome driver app directory
    app_dir = 'Robotics Process Automation Engineer/chromedriver.exe'

    #url for google form
    google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfZ2I7CwNezQmhC0g81es8LPAhAgoeGzmqzT3ud82N8ntHjyQ/viewform?edit_requested=true"
 
    #xpath for signin pop up alert
    signin_alert = "/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span"

    #xpath for email input field
    email_input = '//*[@id="identifierId"]'

    #xpath for next buttton
    next_submit = '//*[@id="identifierNext"]/span/span'

    #xpath for email password input 
    password_input = '//*[@id="password"]/div[1]/div/div[1]/input'

    #xpath for login button
    login_submit = '//*[@id="passwordNext"]'

    #xpath for name input field on the form
    form_name = '//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input'
    
    #xpath for gender selection on the form
    form_gender = '//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[1]/label'
    
    #xpath for email input field on the form
    form_email = '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/input'
    
    #xpath for next button on the form
    form_next_button = '//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div'

    #xpath for school of completion input field on the form
    form_school = '//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input'
    
    #xpath for address input field on the form
    form_address = '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/textarea'
    
    #xpath for phone number input field on the form
    form_phone = '//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/input'
    
    #xpath for comment textarea on the form
    form_comments = '//*[@id="mG61Hd"]/div/div/div[2]/div[5]/div/div[2]/div[1]/div[2]/textarea'
    
    #xpath for the form submission
    #form_submit = '//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]/span'

    #assigning the variable driver to the library and executing brower via the app directory
    driver = webdriver.Chrome(app_dir)
    
    #requesting google
    driver.get(google_form_url)

    #waiting for 5 seconds for the DOM to load
    time.sleep(5)

    #using signin_alert xpath to find and click on the signin 
    driver.find_element_by_xpath(signin_alert).click()
    
    #waiting for 3 seconds for the DOM to load
    time.sleep(3)

    #selecting email input via xpath and inputing details/text(email)
    driver.find_element_by_xpath(email_input).send_keys(details[1])

    #selecting next button and clicking on it
    driver.find_element_by_xpath(next_submit).click()

    #waiting for 3 seconds for the DOM to load
    time.sleep(3)

    #selecting password input via xpath and inputing details/text(password)
    driver.find_element_by_xpath(password_input).send_keys(email_password)

    #selecting  login/submit button and clicking on it
    driver.find_element_by_xpath(login_submit).click()

    #waiting for 3 seconds for the DOM to load
    time.sleep(3)

    #selecting form_name input via xpath and inputing details/text(name)
    driver.find_element_by_xpath(form_name).send_keys(details[0])

    #selecting gender via xpath and clicking on it
    driver.find_element_by_xpath(form_gender).click()

    #selecting form_email input via xpath and inputing details/text(email) 
    driver.find_element_by_xpath(form_email).send_keys(details[1])

    #selecting next button and clicking on it
    driver.find_element_by_xpath(form_next_button).click()

    #selecting form_school input via xpath and inputing details/text(school of completion)
    driver.find_element_by_xpath(form_school).send_keys(details[2])

    #selecting form_address input via xpath and inputing details/text(address)
    driver.find_element_by_xpath(form_address).send_keys(details[3])

    #selecting form_phone number input via xpath and inputing details/text(phone number)
    driver.find_element_by_xpath(form_phone).send_keys(details[4])

    #selecting form_comment textarea via xpath and inputing details/text(comments)
    driver.find_element_by_xpath(form_comments).send_keys(details[5])

    #selecting the sumbit button via xpath and clicking on it
    driver.find_element_by_xpath(form_submit).click()
    
    #waiting for 5 seconds for the DOM to load
    time.sleep(5)

    #closing brower
    driver.close()


#function call
automation()
