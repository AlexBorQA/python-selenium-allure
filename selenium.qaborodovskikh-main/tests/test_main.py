"""
Smoke qaborodovskikh
"""
from selenium.webdriver.common.by import By

def test_label(browser):
    """
    Test case AB-1
    """
        
    browser.get("https://qaborodovskikh.ru/")      
        
    label = browser.find_element(By.XPATH, value="/html/body/header/h1")
    
    assert label.text == "Алексей Бородовских","Unexpected text label name"
    

def test_smoke(browser):
    """
    Test case AB-2
    """
        
    browser.get("https://qaborodovskikh.ru/")
    
    button = browser.find_element(By.CSS_SELECTOR, value='button')
    assert button.text == "Кредо","Unexpected text on button"   
    

def test_button(browser):
    """
    Test case AB-3
    """
        
    browser.get("https://qaborodovskikh.ru/")
    
    button = browser.find_element(By.CSS_SELECTOR, value='button')
    button.click()
    
    assert True
    
    
    
      
    
def test_link_git(browser):
    """
    Test case AB-4
    """
        
    browser.get("https://qaborodovskikh.ru/")
    
    link = browser.find_element(By.XPATH, value="/html/body/main/section[1]/ul/li[5]/a")
    link.click()
    
    assert "AlexBorQA" in browser.title 
    
def test_link_telegram(browser):
    """
    Test case AB-5
    """
        
    browser.get("https://qaborodovskikh.ru/")
    
    link = browser.find_element(By.XPATH, value="/html/body/main/section[1]/ul/li[1]/a")
    link.click()
    
    assert "@Borodovskikh" in browser.title 
    
    
def test_link_vimeo(browser):
    """
    Test case AB-6
    """
        
    browser.get("https://qaborodovskikh.ru/")
    
    link = browser.find_element(By.XPATH, value="/html/body/main/section[2]/ul/li[2]/a")
    link.click()
    
    assert "Alexey Borodovskikh" in browser.title 
        
