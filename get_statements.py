import re
import ast
import html
from bs4 import BeautifulSoup

list_o_dict = []
longString = ""
with open("/Users/mpoltorak/Development/workspace/sec-edgar/SEC-Edgar-Data/BYM/14272/10-K/0000014272-16-000288.txt") as f:
    with open("output.txt", "w") as text_file:
        for line in f:
            if 'CONSOLIDATED STATEMENTS OF EARNINGS - USD' in line:
                for line in f:
                    if '</table>' in line:
                        break
                    if '<tr>' in line:
                        for line in f:
                            longString = longString + line
                            if '</tr>' in line:
                                try:
                                    result = re.search('>(.*)<', longString)
                                    # print(longString)
                                    print(result.group(1))
                                except:
                                    print("non standard")
                                list_o_dict.append(longString)
                                longString = ""
                            if '</table>' in line:
                                break


