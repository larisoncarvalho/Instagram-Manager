from selenium import webdriver
import time
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.instagram.com")

#Enter your instagram username and password here
username=""
password=""

time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
time.sleep(4)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()
time.sleep(5)
if (len(driver.find_elements_by_class_name("piCib"))!=0):
    if(driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")):
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
    
f = open("unfollowlist.txt")
time.sleep(5)
unnames = f.read().split("\n")

unfollowed=0
skipped=0
for uname in unnames:
    driver.get("https://www.instagram.com/"+uname)
    time.sleep(6)
    try:
        try:
            button = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button")
        except:
            try:
                button = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button")
            except:
                print("Already unfollowed "+str(uname))
                skipped= skipped+1
                time.sleep(5)
                continue
        try:
            if ( button.find_element_by_css_selector('span').get_attribute("aria-label") == "Following"):
            button.click()
            time.sleep(5)
                unfollow_button = driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]")
            unfollow_button.click()
            # if("Blocked" in driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div").text):
            #     print("Unfollow Action is blocked")
            #     break
            time.sleep(5)
            print("Unfollowed "+str(uname))
            unfollowed=unfollowed+1
        except:
            print("Already unfollowed "+str(uname))
            skipped= skipped+1
            time.sleep(5)
            continue

    except:
        print("Skipped due to error "+str(uname))
        skipped= skipped+1
        time.sleep(5)
        continue
    time.sleep(5)

driver.close()
print("Unfollowed "+str(unfollowed)+" users, skipped "+str(skipped)+" users")
