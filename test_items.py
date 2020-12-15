import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Список доступных языков: ru, en, es, fr, ar, ca, cs, da, de, en-gb, el, fi, it, ko, nl, pl, pt, pt-br, ro, sk, uk, zh-cn

def test_add_to_shopping_cart(browser):
    '''Запуск браузера по ссылке'''
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')

    def should_be_add_to_cart_button(self):
        '''Проверка наличия кнопки "Добавить в корзину"'''
        assert self.is_element_present(By.CLASS_NAME("btn-add-to-basket"), "#btn_not_present"), "Button 'Add to cart' is not exist"
        #time.sleep(30) # debug для проверки языка.