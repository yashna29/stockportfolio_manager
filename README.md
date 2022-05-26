# Download market data from Yahoo! Finance's API

<table border=1 cellpadding=10><tr><td>

#### \*\*\* IMPORTANT LEGAL DISCLAIMER \*\*\*

---

**Yahoo!, Y!Finance, and Yahoo! finance are registered trademarks of
Yahoo, Inc.**

yfinance is **not** affiliated, endorsed, or vetted by Yahoo, Inc. It's
an open-source tool that uses Yahoo's publicly available APIs, and is
intended for research and educational purposes.

**You should refer to Yahoo!'s terms of use**
([here](https://policies.yahoo.com/us/en/yahoo/terms/product-atos/apiforydn/index.htm),
[here](https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html), and
[here](https://policies.yahoo.com/us/en/yahoo/terms/index.htm)) **for
details on your rights to use the actual data downloaded. Remember - the
Yahoo! finance API is intended for personal use only.**

</td></tr></table>

---

<a target="new" href="https://pypi.python.org/pypi/yfinance"><img border=0 src="https://img.shields.io/badge/python-2.7,%203.6+-blue.svg?style=flat" alt="Python version"></a>
<a target="new" href="https://pypi.python.org/pypi/yfinance"><img border=0 src="https://img.shields.io/pypi/v/yfinance.svg?maxAge=60%" alt="PyPi version"></a>
<a target="new" href="https://pypi.python.org/pypi/yfinance"><img border=0 src="https://img.shields.io/pypi/status/yfinance.svg?maxAge=60" alt="PyPi status"></a>
<a target="new" href="https://pypi.python.org/pypi/yfinance"><img border=0 src="https://img.shields.io/pypi/dm/yfinance.svg?maxAge=2592000&label=installs&color=%2327B1FF" alt="PyPi downloads"></a>
<a target="new" href="https://travis-ci.com/github/ranaroussi/yfinance"><img border=0 src="https://img.shields.io/travis/ranaroussi/yfinance/main.svg?maxAge=1" alt="Travis-CI build status"></a>
<a target="new" href="https://www.codefactor.io/repository/github/ranaroussi/yfinance"><img border=0 src="https://www.codefactor.io/repository/github/ranaroussi/yfinance/badge" alt="CodeFactor"></a>
<a target="new" href="https://github.com/ranaroussi/yfinance"><img border=0 src="https://img.shields.io/github/stars/ranaroussi/yfinance.svg?style=social&label=Star&maxAge=60" alt="Star this repo"></a>
<a target="new" href="https://twitter.com/aroussi"><img border=0 src="https://img.shields.io/twitter/follow/aroussi.svg?style=social&label=Follow&maxAge=60" alt="Follow me on twitter"></a>


**yfinance** offers a threaded and Pythonic way to download market data from [Yahoo!Ⓡ finance](https://finance.yahoo.com).

→ Check out this [Blog post](https://aroussi.com/#post/python-yahoo-finance) for a detailed tutorial with code examples.

[Changelog »](https://github.com/ranaroussi/yfinance/blob/main/CHANGELOG.rst)

---
## Description
The stock portfolio manager program is designed to help an investor manage their portfolio of stock investments. The portfolio is created by asking users to enter the stocks (ticker symbols) that they have invested in, number of shares of each stock and the purchase price per share. This program can be useful to investors in the stock market as they can get real-time data on companies they have invested in. Additionally, they can identify different features of their stock portfolio, such as the total value of their portfolio and unrealized profits/loss. More on this later!

All the data above is stored in multiple one dimensional arrays, which get manipulated to display useful information for the user. The program makes use of the Yahoo! Finance API. This useful API gathers real-time data of stocks, bonds, cryptocurrencies,, and more at the time of execution, precise to the exact hour, minute, and second of the day. The yfinance library was imported from GitHub, where through the given installation process, our devices were able to support the functions of the API and were able to implement it into our program seamlessly.

Using this, the program fetches the current market price for each stock and multiplies the total number of shares per stock to derive the current investment value of each stock. Program also calculates the “Unrealized profit/loss” per stock by subtracting the total purchase price from the current investment value of each stock. The “Total current portfolio” value is then calculated, which is the sum of all stock investment values. The “Total unrealized gain” is also calculated by adding “Unrealized profit/loss” of each stock.

Once the initial portfolio is created, the investor is given a menu of options, where they can refresh their portfolio to see the latest values based on the current market prices. There are also options provided to add or delete stocks, and sort their portfolio by ticker, number of shares, current market price, or investment value in either ascending or descending order. 



## Installation

Install `yfinance` using `pip`:

``` {.sourceCode .bash}
$ pip install yfinance --upgrade --no-cache-dir
```

To install `yfinance` using `conda`, see
[this](https://anaconda.org/ranaroussi/yfinance).

### Requirements

-   [Python](https://www.python.org) \>= 2.7, 3.4+
-   [Pandas](https://github.com/pydata/pandas) (tested to work with
    \>=0.23.1)
-   [Numpy](http://www.numpy.org) \>= 1.11.1
-   [requests](http://docs.python-requests.org/en/master/) \>= 2.14.2
-   [lxml](https://pypi.org/project/lxml/) \>= 4.5.1

### Optional (if you want to use `pandas_datareader`)

-   [pandas\_datareader](https://github.com/pydata/pandas-datareader)
    \>= 0.4.0

---

### Legal Stuff

**yfinance** is distributed under the **Apache Software License**. See
the [LICENSE.txt](./LICENSE.txt) file in the release for details.


AGAIN - yfinance is **not** affiliated, endorsed, or vetted by Yahoo, Inc. It's
an open-source tool that uses Yahoo's publicly available APIs, and is
intended for research and educational purposes. You should refer to Yahoo!'s terms of use
([here](https://policies.yahoo.com/us/en/yahoo/terms/product-atos/apiforydn/index.htm),
[here](https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html), and
[here](https://policies.yahoo.com/us/en/yahoo/terms/index.htm)) for
detailes on your rights to use the actual data downloaded.

---

### P.S.

Please drop me an note with any feedback you have.

**Ran Aroussi**
