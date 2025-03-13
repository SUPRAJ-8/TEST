import os
import sys
import requests
import re
import time
import datetime
from bs4 import BeautifulSoup as bs

# Constants for colors
G = "\u001b[32m"
B = "\u001b[36m"
W = "\033[1;37m"

# Clear terminal
def clear():
    os.system("clear" if "linux" in sys.platform.lower() else "cls")

# Print text with animation
def animation(text):
    for char in text + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

# Print logo
def logo():
    print(f"""\033[1;37m
██████╗░███████╗░█████╗░░██████╗████████╗
██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝
██████╦╝█████╗░░███████║╚█████╗░░░░██║░░░
██╔══██╗██╔══╝░░██╔══██║░╚═══██╗░░░██║░░░
██████╦╝███████╗██║░░██║██████╔╝░░░██║░░░
╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░\u001b[31mv1
\033[1;37m---------------------------------------------
 AUTHOR     : BESAT
 TOOL TYPE  : FILE MAKING
 FACEBOOK.  : BEST DON
 VERSION    :\u001b[32m 2.0\033[1;37m
\033[1;37m----------------------------------------------""")

# Login class
class Login:
    def __init__(self):
        self.session = requests.Session()
        self.cookie = None
        self.token_eaag = None
        self.token_eaab = None
        self.token_eaat = None
        self.initialize()

    def initialize(self):
        clear()
        logo()
        self.ensure_login_directory()
        self.load_or_request_cookie()

    def ensure_login_directory(self):
        """Ensure the 'login' directory exists."""
        if not os.path.exists("login"):
            os.makedirs("login")

    def load_or_request_cookie(self):
        """Load the cookie from file or request it from the user."""
        try:
            with open("login/cookie.json", "r") as f:
                self.cookie = f.read()
            self.token_eaag = open("login/token_eaag.json", "r").read()
            self.token_eaab = open("login/token_eaab.json", "r").read()
            self.token_eaat = open("login/token_eaat.json", "r").read()
            self.validate_cookie()
        except FileNotFoundError:
            self.request_cookie()

    def request_cookie(self):
        """Request the cookie from the user and generate tokens."""
        self.cookie = input(f" [{B}>{W}] ENTER COOKIES: ")
        self.token_eaag = self.generate_token_eaag(self.cookie)
        self.token_eaab = self.generate_token_eaab(self.cookie)
        self.token_eaat = self.generate_token_eaat(self.cookie)
        self.save_tokens()

    def validate_cookie(self):
        """Validate the loaded cookie."""
        try:
            response = self.session.get(
                f"https://graph.facebook.com/me?fields=name,id&access_token={self.token_eaag}",
                cookies={"cookie": self.cookie},
            ).json()
            if "name" in response:
                print(f" [{B}•{W}] Logged in as: {response['name']}")
            else:
                raise ValueError("Invalid cookie or token.")
        except Exception as e:
            print(f" [{B}×{W}] Error validating cookie: {e}")
            self.request_cookie()

    def save_tokens(self):
        """Save tokens to files."""
        try:
            with open("login/cookie.json", "w") as f:
                f.write(self.cookie)
            with open("login/token_eaag.json", "w") as f:
                f.write(self.token_eaag)
            with open("login/token_eaab.json", "w") as f:
                f.write(self.token_eaab)
            with open("login/token_eaat.json", "w") as f:
                f.write(self.token_eaat)
        except Exception as e:
            print(f" [{B}×{W}] Error saving tokens: {e}")

    def generate_token_eaag(self, cookie):
        """Generate EAAG token."""
        url = "https://business.facebook.com/business_locations"
        response = self.session.get(url, cookies={"cookie": cookie})
        try:
            token = re.search(r'(\["EAAG\w+)', response.text).group(1).replace('["', "")
            return token
        except AttributeError:
            print(f" [{B}×{W}] Failed to generate EAAG token. Cookie may be expired.")
            exit()

    def generate_token_eaab(self, cookie):
        """Generate EAAB token."""
        url = "https://www.facebook.com/adsmanager/manage/campaigns"
        response = self.session.get(url, cookies={"cookie": cookie})
        try:
            act_id = re.search(r'act=(.*?)&nav_source', str(response.content)).group(1)
            url = f"{url}?act={act_id}&nav_source=no_referrer"
            response = self.session.get(url, cookies={"cookie": cookie})
            token = re.search(r'accessToken="(.*?)"', str(response.content)).group(1)
            return token
        except Exception as e:
            print(f" [{B}×{W}] Failed to generate EAAB token: {e}")
            return None

    def generate_token_eaat(self, cookie):
        """Generate EAAT token."""
        try:
            data = {
                "access_token": "1348564698517390|007c0a9101b9e1c8ffab727666805038",
                "scope": "",
            }
            response = self.session.post(
                "https://graph.facebook.com/v16.0/device/login/", data=data
            ).json()
            code = response["code"]
            user_code = response["user_code"]
            url = f"https://graph.facebook.com/v16.0/device/login_status?method=post&code={code}&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038"
            response = self.session.get(
                "https://mbasic.facebook.com/device", cookies={"cookie": cookie}
            )
            soup = bs(response.content, "html.parser")
            form = soup.find("form", {"method": "post"})
            data = {
                "jazoest": re.search(r'name="jazoest" type="hidden" value="(.*?)"', str(form)).group(1),
                "fb_dtsg": re.search(r'name="fb_dtsg" type="hidden" value="(.*?)"', str(soup)).group(1),
                "qr": "0",
                "user_code": user_code,
            }
            action_url = "https://mbasic.facebook.com" + form["action"]
            response = self.session.post(action_url, data=data, cookies={"cookie": cookie})
            soup = bs(response.content, "html.parser")
            form = soup.find("form", {"method": "post"})
            data = {}
            for input_tag in form.find_all("input", {"value": True}):
                if input_tag.get("name") != "__CANCEL__":
                    data[input_tag.get("name")] = input_tag.get("value")
            action_url = "https://mbasic.facebook.com" + form["action"]
            self.session.post(action_url, data=data, cookies={"cookie": cookie})
            response = self.session.get(url, cookies={"cookie": cookie}).json()
            return response["access_token"]
        except Exception as e:
            print(f" [{B}×{W}] Failed to generate EAAT token: {e}")
            return None


# Main program
if __name__ == "__main__":
    login = Login()
