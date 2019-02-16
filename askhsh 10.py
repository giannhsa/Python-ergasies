import time, urllib2
run = True
while run:
    #gia na parume ton kwdika selidas
    def gethtml(url):
        try:
            req = urllib2.Request(url)
            return urllib2.urlopen(req).read()
        except Exception, e:
            time.sleep(2)
            return ''
    url = raw_input('Give a url (include http://): ')
    txt = gethtml(url)
    #print(txt)
    from HTMLParser import HTMLParser
    counterlines = 0
    counterlinks = 0
    #gia na metrhsw ta tags
    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == 'p' or tag == 'br' :
                #print tag
                global counterlines
                counterlines += 1
            if tag == 'a' or tag == 'link' :
                global counterlinks
                counterlinks += 1
    parser = MyHTMLParser()
    parser.feed(txt)
    #ektipwsh apotelesmatwn
    print "Allages seiras:", counterlines
    print "Syndesmoi:", counterlinks
    #elegxos
    flag = False
    while flag == False:
        choise = raw_input('Try again? (yes/no)\n')
        if choise == 'yes' :
            run = True
            flag = True
        elif choise == 'no' :
            run = False
            flag = True
        else :
            print "wrong answer!"
