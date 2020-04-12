# 信息校验型反爬虫

#### User-Agent 反爬虫

通过校验 `User-Agent` 来区分爬虫. 它是浏览器的身份标识.

##### 绕过

在请求 `url` 时,加入 `headers` 指定请求头.

```python
import requeste

url = ''
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:62.0) Gecko/20100202 Firefox/62.0'}

response = requeste.get(url, headers=headers)
```

#### Cookie 反爬虫

`Cookie` 可以理解为在HTTP 协议下,服务器或其他脚本语言维护客户端信息的一种方式,是保存在客户端的文本协议,`Cookie` 往往包含客户端或用户的相关信息.

*服务器可以通过校验 `Cookie` 中是否包含指定信息来进行反爬虫.*

##### 绕过

```python
import requeste

url = ''
headers = {'Cookie': 'isfirst=789kq7uc1ppuis'}

response = requeste.get(url, headers=headers)
print(response.status_code)
```

通常会使用 `javascipt` 动态生成验证信息,而不会单纯的重复使用相同的验证信息.

#### 签名验证饭爬虫

签名是根据数据源进行计算或加密的过程,签名的结果是一个具有唯一性和一致性的字符串.签名结果的特性使得它成为验证数据来源和数据完整性的条件,可以有效的避免服务器端将伪造的数据或被篡改的数据当成正常数据处理.

可以通过网络分析查看 `data` 中数据参数,解析加密的过程,用相同的加密方式加密,获得正确的签名验证.

案例:[有道翻译验证](https://github.com/zlj-zz/python_/blob/master/anti-crawl_practice/youdao/youdao.py) 

Youdao web translation signature verifivation bypass case.

常使用 `MD5` 加密方式和 `时间戳` 来用作加密基础.

#### WebSocket 握手验证反爬虫

通过在接受客户端的信息后,加入数据的校验流程,若检验通过则向客户端发送信息,否则不做处理.

信息校验主要解决了客户端身份鉴别,数据来源判断和合法性判断等问题,避免了数据接收者使用被篡改过的数据,保证了数据的有效性.

---

# 动态渲染反爬虫
动态网页比静态网页更具有交互性,能给用户更好的使用体验.动态渲染被广泛的应用在 web 网站中,大部分网站会使用 JavaScript 来提升用户体验.


#### 自动执行的异步请求

异步请求能够减少网络请求的时间,从而提升网页加载的速度.将网页分成若干部分,通过异步请求的方式获取数据,可以提高用户体验,减少用户等待时间.

#### 点击事件和计算

点击事件是指用户的鼠标点击按钮或标签等页面元素的操作,这类事件通常会与一个 `JavaScript` 方法绑定在一起, 这里的计算是指使用 `JavaScript` 计算数值并将结果渲染到网页.

#### 下拉加载和异步请求

下来加载实际上是一种翻页操作,翻页和下拉都是为了查看不同的内容.

#### 通用解决方法
了解了动态渲染之后,我们发现动态渲染的技术多样且组合灵活.如果每次遇到之后都要解析网站,分析 JavaScript 代码逻辑,那么时间成本会很高.会常常出现编辑代码只需要 2 小时,而解析网页却花费好几天的时间.

有没有通用的解决方案吗?

1. **Selenium 套件**. 
    
    Selenium 是一个用于测试 web 程序的自动化工具.我们可以使用 Selenium 和浏览器驱动调用浏览器执行特定的操作.由于调用了浏览器,所以具备了资源自动加载和渲染的能力.
2. **异步渲染库 Puppeteer**.

    使用 Selenium 有一定的缺陷,当我们使用 Python 中的异步库编写爬虫时, Selenium就不是那么合适了.异步是目前提升爬虫效率的常用手段之一,由于浏览器是以进程的方式启动,所以无法满足异步爬虫的渲染需求.因为异步爬虫的请求效率很高,而开启过多的进程是不太现实的.

    Puppeteer 是 Google 开源的 Node 库,更重要的是 Pupeteer 支持异步. Puppeteer 是一个 Node 库, 如果你的爬虫是使用 Node.js 编写的,那么可以直接使用 Puppeteer 支持异步,如果是 Python 写的,需要用支持 Python 的库 Pypeteer.

3. **异步渲染服务 Splash** 

    如果是分布式爬虫,那么在每一台机器上配置 Selenium 和 Pypeteer 是非常麻烦的.Splash 是一个异步的 JavaScript 渲染服务,它是带有 HTTP API 的轻量级 web 浏览器.Splash 能够并行的处理多个页面请求.

---

# 文本混淆反爬虫
文本混淆反爬虫可以有效的避免爬虫获取 web 中 重要的文字信息.

#### 图片伪装反爬虫
图片伪装是指将带有文字的图片和正常的文字混合在一起,达到混淆的效果.它不会影响用户获取信息,但可以让爬虫拿不到真正的数据.

##### 绕过
[用户信息爬取案例](https://github.com/zlj-zz/anti-crawl_case/tree/master/picture_disguise) 

#### CSS 偏移反爬虫
CSS 偏移反爬虫指的是利用 CSS 样式将乱序的文字排版为正常人类阅读理解的顺序.

##### 绕过
[获取机票价格案例](https://github.com/zlj-zz/anti-crawl_case/tree/master/css_offset) 

![css-caset](./css_offset/html/demo-img-1.png) 

#### SVG 映射反爬虫
SVG 是用于描述二位矢量图形的一种图形格式.它基于 xml 描述图形,对图形进行缩放操作都不会i影响图形质量,这个特性导致矢量图被广泛应用与 web 网站中.

##### 绕过
[爬取联系电话案例](https://github.com/zlj-zz/anti-crawl_case/tree/master/SVG_map) 

![SVG-map](./image/SVG-case.png) 
#### 字体反爬虫
以前 web 开发者不惜使用用户计算机上存在的字体,但在 CSS3 时代,开发者可以使用 `@font-face` 为网页指定字体.开发者可以将字体放在 web 服务器上,并在 CSS 样式中使用它.

这种情况下查看源码,会发现一些无法识别的字符,这是 WOFF (Web Open Font Format) 一种网页采用的字体格式标准.我们可以借助 Python 的第三方库 fonttools 将 WOFF 转换成 XML ,这样就可以查看文字的结构和表信息了.安装 fonttools 库:
```shell
pip install fonttools
```
XML 文件中保存的是字形坐标信息,我们无法直接获取结果.可以使用在线字体编辑器查看.

##### 绕过
[字体反爬虫案例](https://github.com/zlj-zz/anti-crawl_case/tree/master/font_anti-crawl) 

#### 文本混淆反爬虫通用解决方法
当我们面对不同文本文本混淆反爬虫时,需要重新分析.如果每一次都要分析,那么开发者会付出很多时间成本.这时我们可以使用光学字符识别 OCR 来帮我们解决文本混淆问题.

---

# 特征识别反爬虫
特征识别反爬虫是指通过客户端的特征,属性或用户行为特点来区分正常用户和爬虫程序的手段.

#### WebDriver 识别
前面了解到爬虫可以借助 web 渲染工具从动态网页中获取数据,其本质就是通过对应的浏览器驱动向浏览器发出行为指令.那么开发者可一根据客户端是否包含驱动这一特征来区分正常用户和爬虫.

##### 绕过
可以通过判断 `Navigator` 对象的 `webdriver` 属性来确认是否通过 WebDriver 驱动浏览器.

**方法一:** `navigator.webdriver` 只适用于使用 WebDriver 的渲染工具,对于 Splash 这种使用 WebKit 内核开发的渲染工具无效.

**方法二:** `navigator.webdriver` 属性是可以更改的,当我们使用 WebDriver 时, `navigator.webdriver` 返回值是 `true` 否则返回 `false` 或 `undefine`.可以通过在触发检测之前更改 `navigator.webdriver` 的值,来绕过检测.
```python
from selenium.webdriver import Chrome

url = 'http://...'
client = Chrome()
client.get(url)
# change property's js
script = '''
    Object.defineProperty(navigator, "webdriver", {get: () => false,});
'''
client.execute_script(script)
    
    ...
```

#### 浏览器特征
判断客户端身份的除了 WebDriver ,还有客户端的操作系统信息和硬件信息等.开发者也可以使用这些特征作为区分条件.

#### 爬虫特征
除了浏览器的属性特征外,爬虫程序也有自身的特点.比如爬虫总是希望用最短时间完成任务.

##### 访问频率限制
访问频率是指单位时间按客户端向服务器发送请求的次数,描述网络请求频繁的程度.正常用户的频率不会像爬虫那么高,开发者可以将访问频率过高的客户端视为爬虫.

可以通过 `time.sleep(NUMBER)` 方法来模拟请求间隔,但实际上爬虫的请求频率是越高越好,所以我们还有其他选择.这就是使用 IP 代理,通过在方式请求时让代理 IP 去帮我们发送请求,我们只需要在本机存储一个 IP 池文件,以便爬虫随时可以从中取出使用.


#### 隐藏链接反爬虫
隐藏链接反爬虫是指在网页中隐藏用于检测爬虫程序的链接的手段.这种链接会被隐藏不会显示在页面中,但爬虫可能会将其放入待爬队列中,并发起请求.开发者可以使用该特征区分两者.

---

# 验证码
验证码是指能够区分用户是计算机或人类的全自动程序.验证码可以有效的防止损害网站利益的行为.验证码的原理很简单:人类有主管意识,能够根据要求执行操作,而计算机不能.

#### 字符验证码
字符验证码是指用数字,字母和标点符号的字符作为元素的图片验证码.它将人类视觉和计算机视觉的差呀作为区分用户身份的依据.

###### 绕过
![demo](./character_verify/image/demo.png) 

[character_verify](https://github.com/zlj-zz/anti-crawl_case/tree/master/character_verify) 使用 PyTesseract 光学图像识别,但其精确度有限.除此之外我们还可以使用深度学习的卷积神经网络训练图像识别模型,使用训练好的模型帮助我们识别,精确度通常高于 PyTesseract.

#### 计算型验证码
计算型验证码实在字符验证码的基础上增加了数学运算,它也是将人类视觉和计算机视觉的差异作为区分用户的依据.

##### 绕过

[calculation-vrify](https://github.com/zlj-zz/anti-crawl_case/tree/master/calculation_vrify) 

Calculation validation bypas case.

you should install `tesseract` and `pytesseract`, if you are `Ubuntu` like:
```shell
sudo apt install tesseract-ocr --fix-missing
sudo apt install libtesseract-dev --fix-missing

pip install pytesseract
```

#### 滑动验证码
开发者试图通过从行为方面区分人机.我们认为计算机难于i准确的完成鼠标点击,拖拽,释放等行为,于是开发了滑动验证码.

##### 绕过

[slide-verify](https://github.com/zlj-zz/anti-crawl_case/tree/master/slide_vrify) 

    Slider validation bypass case.

    you should install `selenium`,like:
    ```shell
    pip install selenium
    ```
#### 滑动拼图验证码
滑动拼图验证码在滑动验证码的基础上增加了随机移动,用户需要使用滑动的方式完成拼图,才能通过验证.

#### 绕过

[slide_jigsaw](https://github.com/zlj-zz/anti-crawl_case/tree/master/slide_jigsaw) 

demo 1 的案例中,目标块使用单独的 div ,这样可以在源码中提取出来,计算获得移动距离.如果将缺口融入到背景之中,那么就可以给爬虫工程师增加难度.在 demo 2 中我们就实现的方式.面对这种情况我们可以使用截图的手段获取前后图片,通过对比获取缺口位置, PIL 库可以帮我们实现这一过程.

#### 文字点选验证码
通过阅读验证要去,去点击对应的文字图片完成验证,这是一种比滑动验证码更难的验证码.

[get should click words](https://github.com/zlj-zz/anti-crawl_case/tree/master/word_click) 

通过 demo 可以获取到要求点击的文字,接着就是识别图像中的文字进行点击.我们可以使用 OCR 光学检测,但实验证明准确率并不高,我们还有其他选择就是通过深度学习的目标检测来识别文字.

#### 鼠标轨迹的检测和原理
鼠标轨迹是鼠标移动的集合,它代表鼠标移动的位置和距离.尽管我们在移动鼠标是已经尽量避免手臂晃动,但还是避免不了细微的晃动.但是当我们使用 Selenium 完成点击事件时,其实只有一个坐标记录,这是由于 Selenium 的定位方式导致的,类似我们点击手机屏幕一样.这个时候开发者就可以根据这种人类使用鼠标是很难完全避免晃动的特点区分正常用户和爬虫程序.开发者可以使用 JavaScript 记录移动滑块时的鼠标坐标信息,然后检测晃动的偏差值(i.e 相邻 `y` 坐标的差值)完成对爬虫程序的检测.

当然,我们也可以模拟晃动的现象,测试代码如下:
```python
from selenium import webdriver

browser = webdriver.Chrome()

url = 'http://www.porters.vip/captcha/mousemove.html'
browser.get(url)

hover = browser.find_element_by_class_name('button1')

action = webdriver.ActionChains(browser)
action.click_and_hold(hover).perform()
action.move_by_offset(100, 3)
action.move_by_offset(40, -5)
action.move_by_offset(10, 3)
action.move_by_offset(5, 2)
action.move_by_offset(10, -1)
action.move_by_offset(30, 3)
action.move_by_offset(55, -2)
action.move_by_offset(10, 1)
action.move_by_offset(30, -6)
action.move_by_offset(20, 4)
action.move_by_offset(15, 2)
action.move_by_offset(15, -7)
action.release().perform()
```

运行结果:

![mouse coordinate](./image/mouse-coordinate.png)
    
运行上面的代码,我们可以看到轨迹线路已经弯曲,但从坐标的记录可以看到远比人移动时产生的坐标数量少.开发者可以利用这一点,但移动的路线是无限的,怎么确定坐标数量呢?我们这里可以通过最短路径来解决,即两点之间一定存在一条最短路径,如果坐标数量少于最短路径的产生的坐标数量则视为爬虫程序.
