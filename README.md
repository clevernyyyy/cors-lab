# cors-lab


## phase one - detection

This portion was taken from https://github.com/RUB-NDS/CORStest and slightly modified for my purposes.  Essentially it sendings an Origin request header and checks the for the Access-Control-Allow-Origin response header to help determine potential vulnerabilities.


## phase two - poc-generation

This is a python script that generates a proof-of-concept HTML file based on user input.