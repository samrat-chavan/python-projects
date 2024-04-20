import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

MAIL_PROVIDER_SMTP_ADDRESS = 'SMTP ADDRESS "smtp.gmail.com"'
MY_EMAIL = "samrat1234@gmail.com"
MY_PASSWORD = "mypassword"

url = "https://shorturl.at/jxyDX"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-price-whole").get_text()
price_without_currency = price.split("₹")[1]
price_as_float = float(price_without_currency)
print(price_as_float)


title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 10,000

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )