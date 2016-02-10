import mechanize, cookielib, random

class anonBrowser(mechanize.Browser):

    def __init__(self, proxies = [], user_agents = []):
        mechanize.Browser.__init__(self)
        self.set_handle_robots(False)        
        self.proxies = proxies + ['http://94.202.58.58:80',\
                                  'http://183.207.228.9:8096'] #These are open proxies found online that were added for testing
        self.user_agents = user_agents + ['Baiduspider+(+http://www.baidu.com/search/spider.htm)',\
            'Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)',\
            'msnbot-webmaster/1.0 (+http://search.msn.com/msnbot.htm)', \
            'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7',\
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)',\
            'Mozilla/5.0 (iPad; CPU OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53',\
            'Mozilla/5.0 (Windows NT 5.1; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; ARM; Trident/6.0; Touch)',\
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:25.0) Gecko/20100101 Firefox/25.0'] 
        self.cookie_jar = cookielib.LWPCookieJar()
	self.set_cookiejar(self.cookie_jar)
        self.anonymize()
	
    def clear_cookies(self):
        self.cookie_jar = cookielib.LWPCookieJar()
        self.set_cookiejar(self.cookie_jar)
    
    def change_user_agent(self):
        index = random.randrange(0, len(self.user_agents) )
        self.addheaders = [('User-agent', \
          ( self.user_agents[index] ))]         
            
    def change_proxy(self):
        if self.proxies:
            index = random.randrange(0, len(self.proxies))
            self.set_proxies( {'http': self.proxies[index]} )
            return self.proxies[index]

    def anonymize(self, sleep = False):
        self.clear_cookies()
        self.change_user_agent()
        ip = self.change_proxy()
        return ip
        if sleep:
            time.sleep(60)


