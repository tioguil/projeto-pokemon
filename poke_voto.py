import json

import requests
from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display

# /usr/bin/chromium-browser
while True:
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    display = Display(visible=0, size=(800, 600))
    display.start()
    browser = webdriver.Chrome()
    # browser = webdriver.PhantomJS()
    browser.get("https://discordbots.org/login?redir=%2Fbot%2F365975655608745985%2Fvote")
    time.sleep(5)
    email_input = browser.find_element_by_xpath("//input[@type='email']")
    email_input.send_keys("EMAIL")

    password_input = browser.find_element_by_xpath("//input[@type='password']")
    password_input.send_keys("SENHA")

    time.sleep(1)
    login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
    login_attempt.submit()

    time.sleep(5)

    btn_authorize = browser.find_element_by_xpath(
        "//button[@type='button'][@class='button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeMedium-1AC_Sl grow-q77ONN']")
    btn_authorize.click()

    time.sleep(5)

    btn_votar = browser.find_element_by_id("votingvoted")
    btn_votar.click()

    time.sleep(5)

    browser.quit()
    display.stop()

    time.sleep(5)
    #URL do canal de texto para sera enviado o p!daily
    url = 'https://discordapp.com/api/v6/channels/591362263257186374/messages'
    headers = {'authority': 'discordapp.com',
               'authorization': 'TOKEN',
               'content-type': 'application/json'}

    data = json.dumps({'content': "p!daily claim"})
    requests.post(url, headers=headers, data=data)

    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    print("Voto em : " + date_time)
    print("Aguardando 12h")

    time.sleep(43210)
