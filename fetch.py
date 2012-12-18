import sys
from subprocess import call

def fetch(url):
    # the laziest way to do this without looking things up
    for i in xrange(0,37):
        call(['wget', url + str(i),'-O',str(i)+'.jpeg'])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Example usage: python fetch.py http://img2.demo.minteye.com/slider/image.ashx?CaptchaId=&w=300&h=250&dumm=634914045520205927&reqid=F46E204D-2C83-4E62-B0EE-490B75FFB64F&img="
        sys.exit()
    url = sys.argv[1]
    fetch(url)

