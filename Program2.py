#Regex for Email
import re
pattern=r"[A-Za-z0-9/.-]+@[\w.-]+.com"
string="please send your feedback at Sajiya8445@gmail.com"
match=re.search(pattern,string)
if match:
    print("email to:", match.group())
else:
    print("no match")
