import requests
import os
import logging
log = logging.getLogger('project')
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

def listfiles(username):
    if os.path.exists(username):
        files = os.listdir(username)
        for file in files:
            print(file)
    else:
        print("No FIles downloaded")

def download(url, name):
    #url = 'https://www.python.org/static/opengraph-icon-200x200.png'
    log.info("Started downloading:{}".format(url))
    r = requests.get(url)
    if not os.path.exists(name):
        os.mkdir(name)
    filename = name+'/'+url.split('/')[-1]
    with open(filename, 'wb') as fp:
        fp.write(r.content)
    log.info("Download COmpleted and stored locally")

def processfile(filepath, usename):
    try:
        if os.path.exists(filepath):
            with open(filepath, 'r') as fp:
                for line in fp:
                    #validate
                    download(line, username)
        else:
            print('File path is wrong try again')
    except Exception as e:
        log.error("There was error:{}".format(str(e)))
        print(e)

#download('https://www.python.org/static/opengraph-icon-200x200.png', 'pavan')
print("Welcome to File manager\n ----------------------\n")
username = input("Enter your username:")
option = int(input("\n1.List of downloads\n2.Download\nEnter your option:"))
if option == 2:
    filepath = input('Enter filename:')
    processfile(filepath, username)
elif option==1:
    listfiles(username)
else:
    print("Choose right option")
