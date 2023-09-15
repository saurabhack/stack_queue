class ArrayStack:
    def __init__(self):
        self.data=[]
    def push(self,d):
        return self.data.append(d)
    def is_empty(self):
        return len(self.data)==0
    def pop(self):
        return self.data.pop()
def is_matched_html(raw):

    S = ArrayStack()
    j = raw.ﬁnd( '<' ) # ﬁnd ﬁrst ’<’ character (if any)
    while j != -1:
        k = raw.find( '>' , j+1)
        if k ==-1:

            return False # invalid tag
            tag = raw[j+1:k]
            if not tag.startswith( '/' ):

                S.push(tag)
            else: # this is closing tag
                if S.is_empty():
                    return False # nothing to match with 15
                if tag[1:] != S.pop():
                    return False # mismatched delimiter
        j = raw.find( '<' , k+1) # ﬁnd next ’<’ character (if any) 18
        return S.is_empty()
print(is_matched_html("<body></body>"))