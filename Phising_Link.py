import requests

def link_check(link):
    def expand_short_url(short_url):
        try:
            response = requests.head(short_url, allow_redirects=True)
            main_url = response.url
            return main_url
        except requests.exceptions.RequestException as e:
            print(f"Error expanding short URL: {e}")
            return None

    # Example usage:
    short_url = link
    return expand_short_url(short_url)


def is_phishing_link(url_list):
    # List of services to create phishing patterns for
    services = [
        "paypal","facebook","google","appleid","ebay","microsoft","amazon","twitter","instagram","linkedin","pinterest","snapchat","tumblr","reddit",
        "youtube","whatsapp","telegram","wechat","line","viber","kik","skype","zoom","discord","twitch","tiktok","quora","flickr","vimeo","badoo","github",
        "myspace","meetup","soundcloud","mix","foursquare","vine","periscope","pof","okcupid","grindr","tinder","hinge","bumble","zoosk","match","eharmony","youtube"
    ]

    for i in services:
        if url_list[0]=='https:' and url_list[1]==i:
            return True
        else:
            continue
    return False
if __name__=='__main__':
    red = "\033[91m"
    green = "\033[92m"
    reset = "\033[0m"
    cyan = "\033[36m"
    print(cyan)
    print("""     ___                                  _     ____
    |_ _|_ __  _ __   ___   ___ ___ _ __ | |_  | __ )  ___  _   _
     | || '_ \| '_ \ / _ \ / __/ _ \ '_ \| __| |  _ \ / _ \| | | |
     | || | | | | | | (_) | (_|  __/ | | | |_  | |_) | (_) | |_| |
    |___|_| |_|_| |_|\___/ \___\___|_| |_|\__| |____/ \___/ \__, |
                                     Nothing is Impossible  |___/""")
    print(reset)
    while True:
        print("1. Check Phishing Link.\n2. Exit.")
        ch=input("Enter Option: ")
        if ch=='1':
            url = input("Enter Url: ")
            print()
            link=link_check(url)
            url_list=[]
            url_list.append(link.split('//')[0])
            url_list.append(link.split('//')[1].split('.')[1])
            if is_phishing_link(url_list):
                print(green,"------> The link appears to be safe.",reset)
                print("Main Url is: ", green,link,reset)
                print()
            else:
                print(red,"------> Warning: This link may be a phishing attempt.")
                print("Main Url is: ",link,reset)
                print()
        else:
            break