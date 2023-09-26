## Project Name: Tweet-My-Speed

### Description
A Python script to automate tweeting your internet speed complaints to your provider when it falls below promised speeds. This project is a part of [100 Days of Code](https://www.udemy.com/course/100-days-of-code/) course, inspired by our instructor [Angel Yu](https://github.com/angelabauer).

### About the Project

After numerous trial and error attempts, I've successfully identified the root of the issue, which primarily lay in selecting the right elements on the web page. The code snippet below showcases what worked for me. I've gone ahead and added comments to each line, so you can get a clear picture of what each step accomplishes.

Now, let me break down the code and provide some insights into why I employed specific techniques.

#### Key Highlights

**1. Secure and Readable:** I use environment variables (ENV) to enhance security by separating sensitive data from the script while improving code readability.

**2. Dual WebDriver Instances:** To keep things organized and easy to manage, I employ two WebDriver instances—one for speed testing and the other for Twitter interaction. This modular approach simplifies code management.

**3. Method Explanation:** Inside the class, you'll notice the introduction of `self.get_up_speed` and `self.get_down_speed`. This addition serves the purpose of comparing internet speeds before triggering a tweet. The idea is to initiate a tweet only when the actual speed falls below the promised speed.

You'll observe that I invoke `self.get_internet_speed()` within the `tweet_at_provider()` method. This is done to facilitate speed comparisons. The script proceeds to send a tweet to the provider only if the live speed from speedtest.net falls short of the promised speed.

While some print statements might not be essential, I've included them for debugging and monitoring purposes, especially when I'm not actively overseeing the script.

#### Understanding Imports

**- Expected Conditions (EC):** These Selenium conditions simplify waiting for elements or conditions to be met, replacing cumbersome time.sleep() commands. Notable conditions include:

- `EC.presence_of_element_located()`: Waits for an element to appear.
- `EC.visibility_of_element_located()`: Waits for an element to become visible.
- `EC.element_to_be_clickable()`: Waits for an element to become clickable for user interaction.

**- NoSuchElementException:** This exception is handled when Selenium can't locate an element using the specified locator.

**- TimeoutException:** This exception manages operations that time out due to specific conditions not being met within a set timeframe.

These measures ensure that our web automation script handles various scenarios gracefully, from slow-loading elements to temporarily missing ones, enhancing its reliability.

Feel free to modify and adapt it to your liking!
