# URL-SHORTNER
# This is a simple URL shortener program that takes a long URL as input and returns a shortened version of it.
import pyshorteners

url = input("Enter the URL to shorten: ")
shortener = pyshorteners.Shortener()
short_url = shortener.tinyurl.short(url)

print("Shortened URL:", short_url)