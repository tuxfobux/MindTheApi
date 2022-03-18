# MindTheApi
Script to generate markdown of API endpoints which then can be used to produce visual mindmap to give a nice overview of the target. Supports txt as well as Burp xml as input.

## Why?
After watching the bug bounty space develop and grow from the side I never noticed any such tool that visualizes the API by its endpoints and makes the researchers life easier to for example document APIs. Recently when I confronted a domain which had multiple big APIs put under it, I thought now is the time. Then the tool born.

## Usage
Input can be supplied with a txt file or Burp Suite's XML output of a single domain.
Text file should have a request type and URL path separated by a space. Also the path **must** start with a single `/`.

Example:
```
GET /callback/braintree?lol
DELETE /consumer-api/venue-content-api/v1/carousels
GET /v1/consumer-api/address-fields/
POST /v1/consumer-api/tab-bar
```

Burp's XML can be supplied as you get it. 

The parser takes care of (removes) parameters, hashes and duplicate lines. 

The stdout output contains the markdown which can be used on a site like https://markmap.js.org/repl/ and visualize everything. There are also code snippets which do that for you or you can export HTML/SVG from the website.

Important note about the mentioned website. It supports max depth of only 6, so the api path which is very "deep"/long won't get put onto the graph. That generally isn't too much of a problem but if it gets really annoying you could build a custome visualizer.

## Output example
Python code could return: 
```
#  callback
## GET braintree
#  consumer-api
##  venue-content-api
###  v1
#### GET carousels
#  v1
## POST checkout-content
```
Another plus is the possibility to easily make notes for every endpoint by just writing after the correct heading line.
Like this:
```
# callback
## GET braintree
returns a random cat image
```
<p>Visualised view:</p>
<img src=visual.png width=500px/>

