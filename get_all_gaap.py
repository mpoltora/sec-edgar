import re
import ast
from bs4 import BeautifulSoup

list_o_dict = []
with open("/Users/mpoltorak/Development/workspace/sec-edgar/SEC-Edgar-Data/BYM/14272/10-K/0000014272-16-000288.txt") as f:
    with open("output.txt", "w") as text_file:
        for line in f:
            if "<us-gaap:" in line and line.__contains__("FD2015") and not line.__contains__("TextBlock") \
                    and not line.__contains__("Policy") and not line.__contains__('Reclassifications') \
                    and not line.__contains__('UseOfEstimates'):

                    reformat = re.compile(r'[\t]').sub('', line)
                    text_file.write(reformat)
                    reformat = re.compile(r'[\t\n]').sub('', line)

                    reformat = re.sub('/', '\',\'', reformat)
                    reformat = re.sub(' ', '\',\'', reformat)
                    reformat = re.sub(':', '\':\'', reformat)
                    reformat = re.sub('=', '\':\'', reformat)
                    reformat = re.sub('<', '', reformat)
                    reformat = re.sub('>', '', reformat)
                    reformat = re.sub('"', '', reformat)
                    reformat = "{'" + reformat + "'}"

                    dictRep = ast.literal_eval(reformat)
                    val = dictRep.get('contextRef')
                    key = val[2:]
                    key = key[:9]
                    key = key + "_" + dictRep.get('us-gaap')
                    dictRep = ast.literal_eval("{'" + key + "':" + reformat + "}")
                    list_o_dict.append(dictRep)

for i in list_o_dict:
    for key, val in i.items():
        for key2, val2 in val.items():
            if key2 == 'unitRef':
                print(key, val2)
