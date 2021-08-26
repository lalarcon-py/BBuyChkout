import time

from selenium import webdriver

driver = webdriver.Firefox()

my_info = {
    "card_info": "1234 26789 10111213",
    "first_name": "FirstName",
    "last_name": "LastName",
    "address": "your address",
    "city": "your city",
    "state": "your state abbreviated", #Make sure to have your state's abbreviation otherwise it will not work i.e Georgia = GA
    "zip": "your zip",
    "email": "your email",
    "phone": "1234567890"
}

url = 'https://www.bestbuy.com/site/macbook-air-13-3-laptop-apple-m1-chip-8gb-memory-256gb-ssd-latest-model-space-gray/5721600.p?skuId=5721600'
driver.get(url)

driver.maximize_window()

driver.execute_script("window.scrollTo(0, 1000)")
time.sleep(5)

click = driver.find_element_by_xpath('/html/body/div[3]/main/div[2]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div/button')
click.click()
time.sleep(5)

checkout = driver.find_element_by_xpath('/html/body/div[7]/div/div[1]/div/div/div/div/div[1]/div[3]/a').click()
checkout
time.sleep(2)

checkout_screen = driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div[2]/div[1]/section[2]/div/div/div[4]/div/div[1]/button')
checkout_screen.click()
time.sleep(4)

continue_as_guest = driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[4]/div/div[2]/button')
continue_as_guest.click()
time.sleep(6)

fname = driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.firstName"]')
lname = driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.lastName"]')
address = driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.street"]')
city = driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.city"]')
state = driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.state"]')
zip = driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.zipcode"]')
email = driver.find_element_by_xpath('//*[@id="user.emailAddress"]')
phone = driver.find_element_by_xpath('//*[@id="user.phone"]')

fname.send_keys('F')
fname.send_keys('i')
fname.send_keys('r')
fname.send_keys('s')
fname.send_keys('t')

lname.send_keys('L')
lname.send_keys('a')
lname.send_keys('s')
lname.send_keys('t')


address.send_keys('A')
address.send_keys('d')
address.send_keys('r')
address.send_keys('r')
address.send_keys('e')
address.send_keys('s')
address.send_keys('s')


city.send_keys('C')
city.send_keys('i')
city.send_keys('t')
city.send_keys('y')

state.send_keys('N')
state.send_keys('V')

zip.send_keys('12345')

email.send_keys('mail@example.com')

phone.send_keys('7251506382')

time.sleep(10)

go = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button')
go.click()
time.sleep(4)

card_info_path = driver.find_element_by_xpath('//*[@id="optimized-cc-card-number"]')
card_info_path.click()
card_info_path.send_keys(my_info['card_info'])

fname_form = driver.find_element_by_xpath('//*[@id="payment.billingAddress.firstName"]')
lname_form = driver.find_element_by_xpath('//*[@id="payment.billingAddress.lastName"]')
address_form = driver.find_element_by_xpath('//*[@id="payment.billingAddress.street"]')
city_form = driver.find_element_by_xpath('//*[@id="payment.billingAddress.city"]')
state_form = driver.find_element_by_xpath('//*[@id="payment.billingAddress.state"]')
zip_form = driver.find_element_by_xpath('//*[@id="payment.billingAddress.zipcode"]')

fname_form.send_keys(my_info['first_name'])

lname_form.send_keys(my_info['last_name'])

address_form.send_keys(my_info['address'])

city_form.send_keys(my_info['city'])

state_form.send_keys(my_info['state'])

zip_form.send_keys(my_info['zip'])
