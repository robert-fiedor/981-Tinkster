from Tkinter import *

import urllib2

gh_url = 'https://api.github.com'

req = urllib2.Request(gh_url)

password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, gh_url, 'user', 'pass')

auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
opener = urllib2.build_opener(auth_manager)

urllib2.install_opener(opener)

handler = urllib2.urlopen(req)

print handler.getcode()
print handler.headers.getheader('content-type')


class MyApp:
    def __init__(self, parent):
        ### 1 -- At the outset, we haven't yet invoked any button handler.
        self.myLastButtonInvoked = None

        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()

        self.yellowButton = Button(self.myContainer1, command=self.yellowButtonClick)
        self.yellowButton.configure(text="YELLOW", background="yellow")
        self.yellowButton.pack(side=LEFT)

        self.redButton = Button(self.myContainer1, command=self.redButtonClick)
        self.redButton.configure(text="RED", background="red")
        self.redButton.pack(side=LEFT)

        self.whiteButton = Button(self.myContainer1, command=self.whiteButtonClick)
        self.whiteButton.configure(text="WHITE", background="white")
        self.whiteButton.pack(side=LEFT)

    def redButtonClick(self):
        print "RED    button clicked.  Previous button invoked was", self.myLastButtonInvoked  ### 2
        self.myLastButtonInvoked = "RED"  ### 1

    def yellowButtonClick(self):
        print "YELLOW button clicked.  Previous button invoked was", self.myLastButtonInvoked  ### 2
        self.myLastButtonInvoked = "YELLOW"  ### 1

    def whiteButtonClick(self):
        print "WHITE  button clicked.  Previous button invoked was", self.myLastButtonInvoked  ### 2
        self.myLastButtonInvoked = "WHITE"  ### 1
        myapp.dothisshit()


    def dothisshit(self):
        gh_url = 'http://vrp.outbrain.com/?transport=jsonp&idsite=6&url=http://www.cnn.com&content_type=text/html&callback=_vrq.jsonp.callbackFn'

        req = urllib2.Request(gh_url)

        password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_manager.add_password(None, gh_url, 'user', 'pass')

        auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
        opener = urllib2.build_opener(auth_manager)

        urllib2.install_opener(opener)

        handler = urllib2.urlopen(req)

        print handler.read()


print "\n" * 100  # a simple way to clear the screen
print "Starting..."
root = Tk()
myapp = MyApp(root)
root.mainloop()
print "... Done!"
