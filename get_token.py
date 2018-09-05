import re
import sys
import argparse
import robobrowser
from yaml import (load, YAMLError)


class TinderToken(object):

    def __init__(self, data):
        """initialise email, password, fb_auth, and user_agent; and call access token function"""

        self.email = data['email']
        self.password = data['password']
        self.fb_auth = data['fb_auth']
        self.user_agent = data['mobile_user_agent']

    def get_access_token(self):
        """returns access token from facebook"""

        # Create a robobrowser instantiation
        brow = robobrowser.RoboBrowser(
            user_agent=self.user_agent,
            parser="lxml")
        brow.open(self.fb_auth)

        # Submit login form
        _form = brow.get_form()
        _form['pass'] = self.password
        _form['email'] = self.email
        brow.submit_form(_form)

        # Click the 'ok' button on the dialog informing you that you have
        # already authenticated with the Tinder app
        _form = brow.get_form()
        brow.submit_form(_form, submit=_form.submit_fields['__CONFIRM__'])

        # Get access token from the HTTP response
        try:
            self.access_token = re.search(
                r"access_token=([\w\d]+)",
                brow.response.content.decode()).groups()[0]
        except NameError:
            print('[!] Cann\'t retreive access token')
            self.access_token = " "

        return self.access_token


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='TinderToken: Get Facebook Access Token for Tinder')

    parser.add_argument(
        '-u',
        '--useconfig',
     help='Use the config file',
     action="store_true")
    parser.add_argument('-e', '--email', help='Using Email Address', type=str)
    parser.add_argument(
        '-p',
        '--password',
     help="Using this password",
     type=str)
    parser.add_argument('-fb', '--fbauth', help='Using this FB-auth', type=str)
    parser.add_argument(
        '-ua',
        '--useragent',
     help='Using this User Agent',
     type=str)

    args = parser.parse_args()

    data = {}
    if args.useconfig:
        with open("config.yml", 'r') as stream:
            try:
                data = load(stream)
            except YAMLError as exc:
                print('[!] FB-auth and User-agent needed in config file...')

    else:
        try:
            data = {
                'email': args.email,
                'password': args.password,
                'fb_auth': args.fbauth,
                'mobile_user_agent': args.useragent
            }
        except Exception as e:
            print('[!] Argument Not Found! {}'.format(e))

    access_token = TinderToken(data).get_access_token()
    print('[*] Required token is: {}'.format(access_token))
