#import sys
#sys.path.append(r"c:\users\username\appdata\local\programs\python\python312\lib\site-packages")

import pyshorteners

def shorten_url(url):
    shortener = pyshorteners.Shortener(timeout=10)  # Set a longer timeout

    try:
        # Try using TinyURL first
        return shortener.tinyurl.short(url)
    except Exception as tiny_error:
        print(f"TinyURL failed: {tiny_error}. Trying with is.gd...")

        try:
            # If TinyURL fails, try using is.gd
            return shortener.isgd.short(url)
        except Exception as isgd_error:
            print(f"is.gd also failed: {isgd_error}.")
            return None  # No provider succeeded

# Ask the user for the URL
long_url = input("Paste your link here: ")

# Try to shorten the link
short_url = shorten_url(long_url)

# Display the result
if short_url:
    print("Your shortened link is: " + short_url)
else:
    print("Failed to shorten the link. Please try again later.")
