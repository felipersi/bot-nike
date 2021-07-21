from selenium import webdriver

nav = webdriver.Chrome()
nav.get('https://unite.nike.com.br/oauth.html?client_id=QLegGiUU042XMAUWE4qWL3fPUIrpQTnq&redirect_uri=https%3A%2F%2Fwww.nike.com.br%2Fapi%2Fv2%2Fauth%2Fnike-unite%2Fset&response_type=code&locale=pt_BR&state=%2Fsnkrs')


email = nav.find_element_by_css_selector('').send_keys('e-mail')
print(email)
email.clear()
print('OK', email)                        
nav.find_element_by_xpath("//input[@name='password']")
nav.find_element_by_xpath("//input[@value='LOG IN']").click()


