import time
from selenium import webdriver
from notify_run import Notify

# Chrome
browser = webdriver.Chrome()

# Worten
# Login
browser.get("https://www.worten.pt/cliente/conta#/myLogin")

#Login info
browser.find_element_by_id("email").send_keys("rockyalife@gmail.com")
browser.find_element_by_id("pass").send_keys("4121994")

time.sleep(5)

acceptCookies = browser.find_element_by_class_name("w-cookies-popup__footer__primary-button")
acceptCookies.click()

time.sleep(1)

enterLogin = browser.find_element_by_class_name("w-button-primary")
enterLogin.click()

time.sleep(2)

browser.get("https://www.worten.pt/gaming/playstation/consolas/ps5/consola-ps5-825gb-7196053")


#browser.get("https://www.worten.pt/gaming/nintendo-switch/consolas-nintendo-switch/consola-nintendo-switch-lite-animal-crossing-32-gb-turquesa-7302248")

buyButton = False

while not buyButton:
    try:
        #If this works then the button is not pytopen
        addToCartBtn = browser.find_element_by_class_name("w-product__actions-info__unavailable")

        #Button isnt open restart script
        print("Button isnt ready yet")

        #Refresh page after sleep
        time.sleep(1)
        browser.refresh()

    except:
        addToCartBtn = browser.find_element_by_class_name("qa-product-options__add-cart-linkto")
        addToCartBtn.click()
        time.sleep(3)

        #Ir para o carrinho e iniciar compra
        browser.get("https://www.worten.pt/carrinho")

        StartOrder = browser.find_element_by_id("cart-continue-btn")
        StartOrder.click()

        #Mobile Notification config at https://notify.run/
        # notify = Notify()
        # notify.send('Há PS5!!!')

        buyButton = True
        
        