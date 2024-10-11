class HistoryNode:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.url)


class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = None

    def visit(self, url: str) -> None:
        if self.cur:
            node = HistoryNode(url)
            self.cur.next = node
            node.prev = self.cur
            self.cur = node
        else:
            self.cur = HistoryNode(url)

    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            steps -= 1
            self.cur = self.cur.prev

        return self.cur.url

    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            steps -= 1
            self.cur = self.cur.next

        return self.cur.url

    def __str__(self):
        res = ''

        cur = self.cur

        while cur.prev:
            cur = cur.prev

        while cur:
            if cur is not self.cur:
                res += str(cur) + '->'
                cur = cur.next
            else:
                res += '**' + str(cur) + '**' + '->'
                cur = cur.next

        return res



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)



browserHistory =  BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       #// You are in "leetcode.com". Visit "google.com"
print(browserHistory)
browserHistory.visit("facebook.com");     #// You are in "google.com". Visit "facebook.com"
print(browserHistory)
browserHistory.visit("youtube.com");      #// You are in "facebook.com". Visit "youtube.com"
print(browserHistory)
browserHistory.back(1);                   #// You are in "youtube.com", move back to "facebook.com" return "facebook.com"
print(browserHistory)
browserHistory.back(1);                   #// You are in "facebook.com", move back to "google.com" return "google.com"
print(browserHistory)
browserHistory.forward(1);                #// You are in "google.com", move forward to "facebook.com" return "facebook.com"
print(browserHistory)
browserHistory.visit("linkedin.com");     #// You are in "facebook.com". Visit "linkedin.com"
print(browserHistory)
browserHistory.forward(2);                #// You are in "linkedin.com", you cannot move forward any steps.
print(browserHistory)
browserHistory.back(2);                   #// You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
print(browserHistory)
browserHistory.back(7);                   #// You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
print(browserHistory)

