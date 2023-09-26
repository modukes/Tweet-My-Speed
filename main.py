import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Define the required internet speed thresholds
UP = 10  # Minimum upload speed in Mbps
DOWN = 150  # Minimum download speed in Mbps

# Load environment variables (you need to set these in your environment)
USERNAME = os.environ.get("USERNAME")
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

# URLs and browser options
SPEED_TEST = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/"

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

# Define a class for the Internet Speed Twitter Bot
class InternetSpeedTwitterBot:
    def __init__(self, upload_speed, download_speed):
        self.driver = webdriver.Edge(options=edge_options)
        self.up = upload_speed
        self.down = download_speed
        self.get_up_speed = 0
        self.get_down_speed = 0

    # Method to get internet speed
    def get_internet_speed(self):
        try:
            # Initialize the Selenium web driver
            driver = webdriver.Edge(options=edge_options)
            driver.get(SPEED_TEST)

            # Find and click the speed test button
            initiate_speed_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'))
            )
            initiate_speed_button.click()

            # Wait for the speed test to complete (adjust time.sleep as needed)
            time.sleep(50)

            # Get the download and upload speeds
            down_speed = driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                             '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
            up_speed = driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                           '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
            self.get_down_speed = float(down_speed)
            self.get_up_speed = float(up_speed)

            print(f"Down = {self.get_down_speed}/ UP = {self.get_up_speed}")

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error getting internet speed: {str(e)}")
        finally:
            driver.quit()

    # Method to tweet at the internet service provider
    def tweet_at_provider(self):
        self.get_internet_speed()

        if self.get_up_speed < self.up or self.get_down_speed < self.down:
            try:
                driver = webdriver.Edge(options=edge_options)
                driver.get(TWITTER_URL)

                # Find and click the sign-in button
                sign_in_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div['
                                                    '1]/div/div[3]/div[5]/a'))
                )
                sign_in_button.click()

                # Enter email and navigate to the username input if it appears
                email = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                    '2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div['
                                                    '2]/div/input'))
                )
                email.send_keys(EMAIL)
                email.send_keys(Keys.ENTER)

                # Check if a username input is present, and if so, enter a username
                username_input = None
                try:
                    username_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        '#layers > div:nth-child(2) > div > div > div > div > div > '
                                                        'div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r'
                                                        '-1xcajam.r-ipm5af.r-g6jmlv > '
                                                        'div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > '
                                                        'div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > '
                                                        'div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r'
                                                        '-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > '
                                                        'div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu > label > div > '
                                                        'div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r'
                                                        '-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input'))
                    )
                except TimeoutException:
                    pass

                if username_input:
                    username_input.send_keys(USERNAME)
                    username_input.send_keys(Keys.ENTER)

                # Enter the password
                password = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#layers > div:nth-child(2) > div > div > div > div > div > '
                                                    'div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r'
                                                    '-1xcajam.r-ipm5af.r-g6jmlv > '
                                                    'div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w'
                                                    '.r-1279nm1.r-htvplk.r-1udh08x > div > div > '
                                                    'div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > '
                                                    'div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r'
                                                    '-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > '
                                                    'div > div.css-1dbjc4n.r-mk0yit.r-13qz1uu > div > label > div > '
                                                    'div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r'
                                                    '-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > '
                                                    'div.css-901oao.r-1awozwy.r-1nao33i.r-6koalj.r-37j5jr.r-1inkyih.r'
                                                    '-16dba41.r-135wba7.r-bcqeeo.r-13qz1uu.r-qvutc0 > input'))
                )
                password.send_keys(PASSWORD)
                password.send_keys(Keys.ENTER)

                # Compose the tweet message
                message = f"Hey Internet Provider, why is my internet speed DOWN: {self.get_down_speed} Mbps/" \
                          f"UP: {self.get_up_speed} Mbps, when I pay for DOWN: {self.down} Mbps/UP: {self.up} Mbps?"

                # Find the tweet input box and send the message
                text = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > div > div > '
                                                                     'div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > '
                                                                     'main > div > div > div > '
                                                                     'div.css-1dbjc4n.r-kemksi.r-1kqtdi0.r-1ljd8xs.r'
                                                                     '-13l2t4g.r-1phboty.r-16y2uox.r-1jgb5lz.r'
                                                                     '-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c '
                                                                     '> div > div.css-1dbjc4n.r-kemksi.r-184en5c > '
                                                                     'div > div.css-1dbjc4n.r-kemksi.r-1h8ys4a > '
                                                                     'div:nth-child(1) > div > div > div > '
                                                                     'div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r'
                                                                     '-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t '
                                                                     '> div:nth-child(1) > div > div > div > div > '
                                                                     'div > '
                                                                     'div.css-1dbjc4n.r-16y2uox.r-bnwqim.r-13qz1uu.r'
                                                                     '-1g40b8q > div > div > div > div > label > '
                                                                     'div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div '
                                                                     '> div > div > div > '
                                                                     'div.DraftEditor-editorContainer > div > div > '
                                                                     'div > div'))
                )
                text.send_keys(message)

                # Find and click the post button
                post_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                '#react-root > div > div > '
                                                'div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div '
                                                '> div > '
                                                'div.css-1dbjc4n.r-kemksi.r-1kqtdi0.r-1ljd8xs.r-13l2t4g.r-1phboty'
                                                '.r-16y2uox.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r'
                                                '-184en5c > div > div.css-1dbjc4n.r-kemksi.r-184en5c > div > '
                                                'div.css-1dbjc4n.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > '
                                                'div > div > '
                                                'div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r'
                                                '-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > '
                                                'div.css-1dbjc4n.r-kemksi.r-jumn1c.r-xd6kpl.r-gtdqiz.r-ipm5af.r'
                                                '-184en5c > div:nth-child(2) > div > div > div:nth-child(2) > '
                                                'div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty'
                                                '.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r'
                                                '-o7ynqc.r-6416eg.r-lrvibr'))
                )
                post_button.click()
                
                # Wait for the tweet to be sent
                time.sleep(10)
                
                if post_button.click():
                    print(f"Tweet Done: {message}")
          
            except (NoSuchElementException, TimeoutException) as e:
                print(f"Error tweeting at the provider: {str(e)}")
            finally:
                driver.quit()

        if self.get_up_speed >= self.up and self.get_down_speed >= self.down:
            print(f"Download Speed: {self.get_down_speed} Mbps")
            print(f"Upload Speed: {self.get_up_speed} Mbps")

# Create an instance of the bot and call the tweet_at_provider method
bot = InternetSpeedTwitterBot(UP, DOWN)
bot.tweet_at_provider()
