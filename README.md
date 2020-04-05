# Information verification type anti-reptile

## User-Agent Anti-Crawler

Identify crawlers by verifying `User-Agent`. It is the identity of the browser.

### Bypass

When requesting url, add headers to specify the request header.

```python
import requeste

url = ''
headers = {'User-Agent': 'Mozilla / 5.0 (X11; Linux x86_64; rv: 62.0) Gecko / 20100202 Firefox / 62.0'}

response = requeste.get (url, headers = headers)
```

## Cookie anti-reptile

`Cookie` can be understood as a way for the server or other scripting languages ​​to maintain client information under the HTTP protocol, which is a text protocol stored on the client.`Cookie` often contains information about the client or user.

> *The server can perform anti-reptile by verifying whether the specified information is included in the `Cookie`.*

### Bypass

```python
import requeste

url = ''
headers = {'Cookie': 'isfirst = 789kq7uc1ppuis'}

response = requeste.get (url, headers = headers)
print (response.status_code)
```

Usually, javascipt is used to dynamically generate verification information, rather than simply reusing the same verification information.

## Signature verification rice crawler

Signature is the process of calculating or encrypting according to the data source. The result of the signature is a unique and consistent string. The characteristics of the signature result make it a condition for verifying the data source and data integrity, which can effectively avoid the server side Treat forged data or tampered data as normal data.

You can view the data parameters in `data` through network analysis, analyze the encryption process, and encrypt with the same encryption method to obtain the correct signature verification.

Case: [Youdao Translation Verification](https://github.com/zlj-zz/python_/blob/master/anti-crawl_practice/youdao/youdao.py)

The `MD5` encryption method and timestamp are often used as the basis for encryption.

## WebSocket handshake verification anti-reptile

After accepting the client's information, join the data verification process.If the verification is passed, the information is sent to the client, otherwise no processing is performed.

Information verification mainly solves the problems of client identity authentication, data source judgment and legality judgment, avoids the use of tampered data by the data receiver, and ensures the validity of the data.

---

# Dynamic rendering anti-reptile

## Common Dynamic Rendering Anti-Crawler Cases

### Automatically executed asynchronous requests

Asynchronous requests can reduce the time of network requests, thereby increasing the speed of web page loading. Dividing the web page into several parts and obtaining data through asynchronous requests can improve the user experience and reduce user waiting time.

### Click events and calculations

Click event refers to the operation of the user's mouse click on a button or label and other page elements. This type of event is usually bound to a JavaScript method. The calculation here refers to the use of JavaScript to calculate the value and render the result to the web page. .

### Drop-down loading and asynchronous requests

Down-loading is actually a page-turning operation, both page-turning and drop-down are for viewing different content.

## General solution
