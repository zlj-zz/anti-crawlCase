# Information verification type anti-crawl

#### User-Agent Anti-Crawler

Identify crawlers by verifying `User-Agent`. It is the identity of the browser.

##### Bypass

When requesting url, add headers to specify the request header.

```python
import requeste

url = ''
headers = {'User-Agent': 'Mozilla / 5.0 (X11; Linux x86_64; rv: 62.0) Gecko / 20100202 Firefox / 62.0'}

response = requeste.get (url, headers = headers)
```

#### Cookie anti-crawl

`Cookie` can be understood as a way for the server or other scripting languages to maintain client information under the HTTP protocol, which is a text protocol stored on the client.`Cookie` often contains information about the client or user.

* The server can perform anti-reptile by verifying whether the specified information is included in the `Cookie`. *

##### Bypass

```python
import requeste

url = ''
headers = {'Cookie': 'isfirst = 789kq7uc1ppuis'}

response = requeste.get (url, headers = headers)
print (response.status_code)
```

Usually, javascipt is used to dynamically generate verification information, rather than simply reusing the same verification information.

#### Signature verification rice crawler

Signature is the process of calculating or encrypting according to the data source. The result of the signature is a unique and consistent string. The characteristics of the signature result make it a condition for verifying the data source and data integrity, which can effectively avoid the server side Treat forged data or tampered data as normal data.

You can view the data parameters in `data` through network analysis, analyze the encryption process, and encrypt with the same encryption method to obtain the correct signature verification.

Case: [Youdao Translation Verification](https://github.com/zlj-zz/python_/blob/master/anti-crawl_practice/youdao/youdao.py)

Youdao web translation signature verifivation bypass case.

The MD5 encryption method and timestamp are often used as the basis for encryption.

#### WebSocket handshake verification anti-crawl

After accepting the client's information, join the data verification process.If the verification is passed, the information is sent to the client, otherwise no processing is performed.

Information verification mainly solves the problems of client identity authentication, data source judgment and legality judgment, avoids the use of tampered data by the data receiver, and ensures the validity of the data.

---

# Dynamic rendering anti-crawl
Dynamic web pages are more interactive than static web pages and can give users a better user experience. Dynamic rendering is widely used in web sites, and most sites will use `JavaScript` to enhance the user experience.


#### Automatically executed asynchronous requests

Asynchronous requests can reduce the time of network requests, thereby increasing the speed of web page loading. Dividing the web page into several parts and obtaining data through asynchronous requests can improve the user experience and reduce user waiting time.

#### Click events and calculations

Click event refers to the operation of the user's mouse click on a button or label and other page elements. This type of event is usually bound to a JavaScript method. The calculation here refers to the use of JavaScript to calculate the value and render the result to the web page. .

#### Drop-down loading and asynchronous requests

Down-loading is actually a page-turning operation, both page-turning and drop-down are for viewing different content.

#### General solution
After understanding the dynamic rendering, we found that the dynamic rendering technology is diverse and flexible. If you have to parse the website and analyze the JavaScript code logic after each encounter, the time cost will be high. It will often appear that editing the code only takes 2 hours, But parsing the webpage took several days.

Is there a general solution?

1. **Selenium Suite** 

    Selenium is an automated tool for testing web programs. We can use Selenium and the browser driver to call he browser to perform specific operations. Since the browser is called, it has the ability to automatically load and render resources.

2. **Asynchronous rendering library Puppeteer**  

    Using Selenium has certain flaws. When we use the asynchronous library in Python to write a crawler, Selenium is not so suitable. Asynchrony is one of the common methods for improving the efficiency of crawlers. Because the browser is started in a process, it cannot Meet the rendering needs of asynchronous crawlers. Because asynchronous crawlers have high request efficiency, it is not realistic to start too many processes.

    Puppeteer is Google's open source Node library, and more importantly, Pupeteer supports asynchronous. Puppeteer is a Node library. If your crawler is written using Node.js, you can directly use Puppeteer to support asynchronous. If it is written in Python, you need to use Pypeteer, a library that supports Python.

3. **Asynchronous rendering service Splash**

    If it is a distributed crawler, it is very troublesome to configure Selenium and Pypeteer on each machine. Splash is an asynchronous JavaScript rendering service, which is a lightweight web browser with HTTP API. Splash can process in parallel Multiple page requests.

---

# Text confusion anti-crawl
Text confusion anti-reptiles can effectively prevent crawlers from obtaining important text information on the web.

#### Picture camouflage anti-crawl
Picture disguise refers to mixing pictures with text and normal text together to achieve the effect of confusion. It does not affect the user's access to information, but it can prevent the crawler from getting real data.

##### Bypass
[User Information Crawling Case](https://github.com/zlj-zz/anti-crawl_case/tree/master/picture_disguise)

#### CSS Offset Anti-Crawler
CSS offset anti-reptile refers to the use of CSS styles to typeset out-of-order text into the order of normal human reading and understanding.

##### Bypass
[Get air ticket price case](https://github.com/zlj-zz/anti-crawl_case/tree/master/css_offset)

![css-caset](./css_offset/html/demo-img-1.png)

#### SVG mapping anti-reptile
SVG is a graphic format used to describe two-bit vector graphics. It describes graphics based on xml, and scaling operations on the graphics will not affect the quality of the graphics. This feature causes vector graphics to be widely used in web sites.

##### Bypass
[Crawl contact phone case](https://github.com/zlj-zz/anti-crawl_case/tree/master/SVG_map)

![SVG-map](./image/SVG-case.png)
#### Font anti-reptile
In the past, web developers did not hesitate to use fonts that existed on users' computers, but in the era of CSS3, developers can use `@font-face` to specify fonts for web pages. Developers can put fonts on a web server and use them in CSS styles it.

In this case, if you look at the source code, you will find some unrecognized characters. This is a font format standard used by WOFF (Web Open Font Format). We can use Python's third-party library fonttools to convert WOFF to XML, so that You can view the text structure and table information. Install the fonttools library:
```shell
pip install fonttools
```
The XML file contains the glyph coordinate information, we cannot directly obtain the results. You can use the online font editor to view.

##### Bypass
[Font Anti-Crawler Case](https://github.com/zlj-zz/anti-crawl_case/tree/master/font_anti-crawl)

#### General solution to text confusion anti-reptile
When we are faced with different text and text confusion anti-reptiles, we need to re-analyze. If we have to analyze each time, then developers will pay a lot of time costs. At this time, we can use optical character recognition OCR to help us solve the text confusion problem.

---
 
# Feature recognition anti-reptile
Feature recognition anti-reptile refers to the means to distinguish normal users from crawler programs through the characteristics, attributes or user behavior characteristics of the client.

#### WebDriver recognition
I learned earlier that crawlers can use web rendering tools to obtain data from dynamic web pages. The essence is to issue behavior instructions to the browser through the corresponding browser driver. Then developers can distinguish normal users according to whether the client includes a driver. And reptiles.

##### Bypass
You can confirm whether the browser is driven by WebDriver by judging the `webdriver` property of the `Navigator` object.

**Method 1:** `navigator.webdriver` is only applicable to the rendering tool using WebDriver, and it is not valid for the rendering tool developed using WebKit kernel such as Splash.

**Method 2:** The property of `navigator.webdriver` can be changed. When we use WebDriver, the return value of `navigator.webdriver` is `true`, otherwise it returns` false` or `undefine`. It can be detected by triggering Change the value of `navigator.webdriver` before to bypass detection.
```python
from selenium.webdriver import Chrome

url = 'http: // ...'
client = Chrome ()
client.get (url)
# change property's js
script = '''
    Object.defineProperty (navigator, "webdriver", {get: () => false,});
'''
client.execute_script (script)
    
    ...
```

#### Browser Features
In addition to WebDriver, the client's operating system information and hardware information are also used to determine the identity of the client. Developers can also use these characteristics as a distinction condition.

#### Crawler features
In addition to the attribute characteristics of the browser, the crawler program also has its own characteristics. For example, the crawler always wants to complete the task in the shortest time.

##### Access frequency limitation
The frequency of access refers to the number of requests sent by the client to the server per unit time, describing the frequency of network requests. The frequency of normal users is not as high as that of crawlers. Developers can treat clients with too high access frequency as crawlers.

You can use the `time.sleep(NUMBER)` method to simulate the request interval, but in fact the request frequency of the crawler is as high as possible, so we have other options. This is the use of IP proxy, by letting the proxy IP when requesting in the way To help us send requests, we only need to store an IP pool file locally so that the crawler can be taken out of it at any time.


#### Hidden link anti-crawl
Hidden link anti-crawler refers to a method of hiding links used to detect crawler programs in web pages. Such links will be hidden and will not be displayed on the page, but the crawler may put it in the queue to be crawled and initiate a request. Developers can use this feature to distinguish between the two.

---

# Captcha
The verification code refers to a fully automatic program that can distinguish whether the user is a computer or a human. The verification code can effectively prevent behavior that harms the interests of the website. The principle of the verification code is simple: humans are competent and can perform operations according to requirements, while computers cannot.

#### Character verification code
Character verification code refers to the picture verification code that uses numbers, letters and punctuation characters as elements. It uses the difference between human vision and computer vision as the basis for distinguishing users' identities.

###### Bypass
![demo](./character_verify/image/demo.png)

[character_verify](https://github.com/zlj-zz/anti-crawl_case/tree/master/character_verify)

uses PyTesseract optical image recognition, but its accuracy is limited. In addition, we can also use deep learning volumes The product neural network trains the image recognition model and uses the trained model to help us identify.The accuracy is usually higher than PyTesserct.

#### Computation verification code
The computational verification code adds mathematical operations to the character verification code.It is also based on the difference between human vision and computer vision as the basis for distinguishing users.

##### Bypass

[calculation-vrify](https://github.com/zlj-zz/anti-crawl_case/tree/master/calculation_vrify)

Calculation validation bypas case.

you should install `tesseract` and` pytesseract`, if you are `Ubuntu` like:
```shell
sudo apt install tesseract-ocr --fix-missing
sudo apt install libtesseract-dev --fix-missing

pip install pytesseract
```

#### Slide verification code
Developers tried to distinguish human-machine by behavior. We think it is difficult for computers to accurately complete mouse clicks, drags, and releases, so we developed a sliding verification code.

##### Bypass

[slide-verify](https://github.com/zlj-zz/anti-crawl_case/tree/master/slide_vrify)

    Slider validation bypass case.

    you should install `selenium`, like:
    `` `shell
    pip install selenium
    `` `
#### Sliding puzzle verification code
The sliding puzzle verification code adds random movement to the sliding verification code.The user needs to use the sliding method to complete the puzzle to pass the verification.

#### Bypass

[slide_jigsaw](https://github.com/zlj-zz/anti-crawl_case/tree/master/slide_jigsaw)

In the case of demo 1, the target block uses a separate `div`, which can be extracted from the source code and calculated to obtain the moving distance. If the gap is integrated into the background, then it can increase the difficulty for the crawler engineer. Implementation method. In this situation, we can use screenshots to obtain the front and rear pictures, and obtain the gap position by comparison.The PIL library can help us achieve this process.

#### Text click verification code
Go through reading verification, go to click the corresponding text picture to complete verification, this is a harder verification code than sliding verification code.

[get should click words](https://github.com/zlj-zz/anti-crawl_case/tree/master/word_click)

Through the demo, you can get the text that you want to click, and then the text in the image is recognized to click. We can use OCR optical detection, but the experiment proves that the accuracy is not high, and we have other options to identify through deep learning target detection Text.

#### Mouse track detection and principle
The mouse track is a collection of mouse movements, which represents the position and distance of the mouse movement. Although we have tried to avoid the shaking of the arm when moving the mouse, it still can not avoid the slight shaking. But when we use Selenium to complete the click event, there is actually only one Coordinate records, this is due to the positioning method of Selenium, similar to when we click on the screen of the mobile phone. At this time, the developer can distinguish the normal user from the crawler program according to the characteristic that it is difficult for the human to use the mouse to avoid shaking completely. The developer can Use JavaScript to record the mouse coordinate information when moving the slider, and then detect the deviation value of the shaking (i.e. the difference between the adjacent y coordinates) to complete the detection of the crawler program.

Of course, we can also simulate the phenomenon of shaking, the test code is as follows:
```python
from selenium import webdriver

browser = webdriver.Chrome ()

url = 'http://www.porters.vip/captcha/mousemove.html'
browser.get (url)

hover = browser.find_element_by_class_name ('button1')

action = webdriver.ActionChains (browser)
action.click_and_hold (hover) .perform ()
action.move_by_offset (100, 3)
action.move_by_offset (40, -5)
action.move_by_offset (10, 3)
action.move_by_offset (5, 2)
action.move_by_offset (10, -1)
action.move_by_offset (30, 3)
action.move_by_offset (55, -2)
action.move_by_offset (10, 1)
action.move_by_offset (30, -6)
action.move_by_offset (20, 4)
action.move_by_offset (15, 2)
action.move_by_offset (15, -7)
action.release (). perform ()
```

operation result:

![mouse coordinate](./image/mouse-coordinate.png)
    
Running the above code, we can see that the trajectory line has been bent, but from the record of coordinates, we can see that it is far less than the number of coordinates generated when people move. Developers can use this, but the route of movement is unlimited, how to determine What about the number of coordinates? We can solve it by the shortest path here, that is, there must be a shortest path between two points.If the number of coordinates is less than the number of coordinates generated by the shortest path, it is regarded as a crawler program.
