import re
def text_preprocess(texts):
    # 保留有用的中英文字符和部分标点
    ptexts = []
    for text in texts:
        ptext = text
        # 去除html标签/包括尖括号的标签
        ptext = re.sub(u"</?\w+[^>]*>","",ptext) 
        # 去除包括方括号的标签
        ptext = re.sub(u'\[[^\u4E00-\u9FFF]*\]'," ",ptext)
        # 去除网址
        ptext = re.sub(u"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+","",ptext)
        # 只保留中英文数字和部分标点符号
        ptext = re.sub(u"[^\u4E00-\u9FFF^，:：。\-？,.?^a-z^A-Z^0-9]", " ", ptext)
        # 英文大小写统一为小写
        ptext = ptext.lower()
        # 去除单个英文字符
        ptext = re.sub(u"\s[a-z]\s","",ptext)
        # 去除某些无意义英文字符
        ptext = re.sub(u"nbsp|br|div","",ptext)
        # 去除多余空格
        ptext = re.sub(u"[\s]{2,}"," ",ptext)
        # 去除多余-
        ptext = re.sub(u"[\-]{2,}","",ptext)
        # 去除字符串两边空字符
        ptext = ptext.strip()

        ptexts.append(ptext)
    return ptexts

if __name__=="__main__":
    texts = ["<br>应用名称：app;[br]应用包名：sounds;应用版本[src = 876.app.com]&nbsp&br&div：0.0.7;唯一标识：312c3008ae47d;错误代码：40111;加固时间：2019-11-1 22:52:48;为什么老是系统故障啊！http://163.buzhi.com.cn error bug"]
    print('texts: ',texts)
    print('ptexts: ',text_preprocess(texts))
