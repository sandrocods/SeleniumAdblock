
# SeleniumAdblock

A Package to block ads and popups in your automation testing, inspired from [puppeteer-extra-plugin-adblocker](https://github.com/berstend/puppeteer-extra/tree/master/packages/puppeteer-extra-plugin-adblocker) Javascript, 
here i make it in python3 version for Chrome Browser


## Acknowledgements

 - [AdBlock — best ad blocker](https://chrome.google.com/webstore/detail/adblock-%E2%80%94-best-ad-blocker/gighmmpiobklfepjocnamgkkbiglidom)
 - [Ultimate Ad Blocker](https://chrome.google.com/webstore/detail/ultimate-ad-blocker/jfhbealifiddpdbakoaogajmffjdonie?gclid=CjwKCAiAjs2bBhACEiwALTBWZbsiuez7GthCiQlR9PcEEY5e6yYCjCjjeHELeCCLsRIgtkvWGIVnyhoCve4QAvD_BwE)
 - [Popup Blocker (strict)](https://chrome.google.com/webstore/detail/popup-blocker-strict/aefkmifgmaafnojlojpnekbpbmjiiogg)

## Feature

| Name             |  |
| ----------------- | - |
| Small Size Package | ✔ |
| Automatic Install to Chrome | ✔ |
| Block Ads | ✔ |
| Block Popup | ✔ |
| Block Redirect | ✔ |


## Demo

#### Without SeleniumAdblocker
https://user-images.githubusercontent.com/59155826/201874080-865fb388-b255-4539-9a61-c47dbe52bc78.mp4

#### With SeleniumAdblocker
https://user-images.githubusercontent.com/59155826/201874212-671f2778-b681-4b2b-be65-28c0264f164f.mp4

## Installation

Installation from source (requires git):

```bash
  git clone https://github.com/sandrocods/SeleniumAdblock
  cd SeleniumAdblock
  python setup.py install
```

or :
```bash
  pip install git+https://github.com/sandrocods/SeleniumAdblock.git
```

## Writing Code

```python
  from selenium import webdriver
  import SeleniumAdblock
```

After import package , create an instance of the SeleniumAdblock class.

```python
  options = SeleniumAdblock.SeleniumAdblock()._startAdBlock()
  # options.add_argument('--disable-blink-features=AutomationControlled')
```
in options you can add more arguments

`Dont add options.add_argument("--disable-extensions") because it will disable the adblock extension`


```python
  driver = webdriver.Chrome(options=options) 
  driver.get("https://www.detik.com/")
```

Example Code : [example.py](https://github.com/sandrocods/SeleniumAdblock/blob/master/example/example.py)

## API Reference

#### Get all list extension in this package

```python
import SeleniumAdblock

options = SeleniumAdblock.SeleniumAdblock()
for i in options._listaAdBlock():
    print(i)

```

#### Start with Another Adblock 

```python
import SeleniumAdblock

options = SeleniumAdblock.SeleniumAdblock()._startAdblockList(
    name="AdBlock-best-ad-blocker"
)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. Name from _listaAdBlock() |



#### Start with Custom extension

```python
import SeleniumAdblock

options = SeleniumAdblock.SeleniumAdblock()._startCustomAdBlock(
    path=r"C:\Users\user\Downloads\Ultimate-Ad-Blocker.crx"
)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `path`      | `string` | **Required**. path of extension  |

## Running Tests

To run tests, run the following command

```bash
  cd test
  python3 testAdblock.py
```


## Support

For support, email krisandromartinus@gmail.com / telegram : @sandroputraaa
