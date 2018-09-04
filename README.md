## Generate Access Token For Tinder
Generate access token for Tinder using credentials from Facebook

### Argparse Usage

```console
gavy42@jarvis:~/Desktop/tinder-token-retriever$ python3 get_token.py  -h
usage: get_token.py [-h] [-u] [-e EMAIL] [-p PASSWORD] [-fb FBAUTH]
                    [-ua USERAGENT]

TinderToken: Get Facebook Access Token for Tinder

optional arguments:
  -h, --help            show this help message and exit
  -u, --useconfig       Use the config file
  -e EMAIL, --email EMAIL
                        Using Email Address
  -p PASSWORD, --password PASSWORD
                        Using this password
  -fb FBAUTH, --fbauth FBAUTH
                        Using this FB-auth
  -ua USERAGENT, --useragent USERAGENT
                        Using this User Agent
```

### Usage

1. Run `pip3 install -r requirements.txt` to install required modules.
2. Edit your _email_ and _password_ in `config.yml` file.
3. Run `python3 get_token.py -u` to get token whilst using login details from configuration file.