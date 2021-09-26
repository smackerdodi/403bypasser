# 403bypasser
automate the procedure of 403 response code bypass
# Description 
i notice a lot of #bugbountytips describe how to bypass 403 response code so when i collect all methods i have found that i need more than 40 request to handle all methods . so as i love automating i have created this tool to do the heavy work . but as i also recommend you need later to check it manually 

The tool use three technique to try to bypass 403 response code and give out the response code for each retry in coloured output to be easy to read :

1- use multiple request methods ( GET - POST- HEAD... etc)

2- use multiple payloads at the end of URL (kudos to those who tweet these tips)

3- add headers to the request (X-Forwarded-Host , X-Host ... etc )

# Installation :

1- git clone https://github.com/smackerdodi/403bypasser.git

2- cd 403bypasser

3- pip3 install -r requirements.txt

# Usage 

the tool take two arguments : url - path 

python3 403bypasser.py url path

EX : python3 403bypasser.py https://www.example.com/ admin results.txt ( space between url and path and results)

# Todo :

make this tool deal with multiple threads and take a list of URLs not just one URL 

# what you can do :

If you get a bounty out of this tool . whatever your relegion is please pray for me 
