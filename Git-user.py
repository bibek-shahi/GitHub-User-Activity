import sys
import urllib.request
import json
user_name = ""

if len(sys.argv) == 2:
    user_name = sys.argv[1]
    #print(f"GitHub username:{user_name}")

#Making URL
    try:
        url = f'https://api.github.com/users/{user_name}/events'
        response = urllib.request.urlopen(url)
        source = response.read()
        data = json.loads(source)

        for items in data:

            if items['type'] == 'PushEvent':

                print(f" Pushed to :{items['repo']['name']}")

            elif items['type'] == 'PullRequestEvent':
                print(f"{items['payload']['action']} a pull request in  :{items['repo']['name']}")

            elif items['type'] == 'WatchEvent':
                print(f"Starred a repo  :{items['repo']['name']}")

        #print(json.dumps(data, indent=4))


    except Exception:

            print(f"GitHub username:{user_name} not found")



else :

    print("Usage: python main.py <username>")
