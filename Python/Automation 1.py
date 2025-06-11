from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\Rajat Rane\Desktop\Java VS Code\chromedriver.exe')
driver.maximize_window()
driver.get('https://whatsapp.com')
driver.minimize_window()
print(driver.title)
print(driver.current_url)