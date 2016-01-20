from selenium import webdriver

print('Lets Go! Enter your email')
userEmail = raw_input()
print('Enter your password')
userPassword = raw_input()

browser = webdriver.Firefox()
browser.get('https://login.microsoftonline.com/')

emailElem = browser.find_element_by_id('cred_userid_inputtext')
emailElem.send_keys(userEmail)

passwordElem = browser.find_element_by_id('cred_password_inputtext')
passwordElem.send_keys(userPassword)

signInElem = browser.find_element_by_id('cred_sign_in_button')
passwordElem.submit()