from selenium import webdriver
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class WhatsappBot:
    def __init__(self):
        self.menssage = "Teste de automação de WhatsApp"
        self.grupos = ["escola", "familia", "amigos"]
        binary = FirefoxBinary("/usr/lib/firefox/firefox")
        options = webdriver.FirefoxOptions()
        opts = Options()
        opts.headless = True
        driver = webdriver.Firefox(options=opts)
        options.add_argument('lang=pt-br')
        cap = DesiredCapabilities().FIREFOX
        #cap["marionette"] = False
        self.driver = webdriver.Firefox(capabilities=cap,firefox_binary=binary, executable_path="/usr/bin/geckodriver", firefox_options=options)
        #cap = DesiredCapabilities().FIREFOX
        #cap["marionette"] = False
        #binary = FirefoxBinary("/usr/bin/firefox")
        #self.drive = webdriver.Firefox(capabilities=cap, firefox_binary=binary, executable_path="/usr/bin/geckodriver",  firefox_options=options)

    def SendMenssage(self):
        #<span dir="auto" title="Ilana" class="_3ko75 _5h6Y_ _3Whw5">Ilana</span>
        #<div tabindex="-1" class="_3uMse">
        #<span data-testid="send" data-icon="send" class="">
        time.sleep(40)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse')eatedException: Message: Unable to find a matching set of capabilities

[pc@pcbombado whatsapp]$ 
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.menssage)
            time.sleep(3)
            send_buttom = self.driver.find_element_by_xpath('span[@data-icon="send"]')
            time.sleep(3)
            send_buttom.click()
            time.sleep(5)
            
bot = WhatsappBot()
bot.SendMenssage()