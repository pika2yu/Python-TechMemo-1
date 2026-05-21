#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#*****************************************
# Python の比較 
#*****************************************
# 括弧で括らず : と indent で記述していく以外、基本は Java と同じ。
# いくつかユニークな比較演算子や文がある。
# - is / is not
# - in / not in
# - pass文
# - Java の else if は elif
#


# In[ ]:


#------------------------------
# is / is not
#------------------------------
# リストなどの参照型の比較に使う
#                          Java       Python
#  同じオブジェクトかの比較     ==         is
#    (アドレスの比較)
#  同じ値かの比較            equals      == 
#
# 値を比較したいのであれば == を使う。
# 比較対象が参照型でオブジェクトが同一かを比較したい時はisを使う。
# 関数の戻り値の None と比較するときは is / is not
# 参照型でない変数では is も == も結果は同じであるが、上記の原則に沿うのが良い。
#


# In[23]:


a = [1, 2, 3]
b = [1, 2, 3]

# == で値の比較なら一致
print('==で比較')
if a==b:
    print(' 一致')
else:
    print(' 不一致')
# is で値の比較だと不一致
print('is で比較')
if a is b:
    print(' 一致')
else:
    print(' 不一致')


# In[24]:


#---------------------
# 紛らわしい例
# 以下のように値が同じでも is と == の結果が異なるので、何を比較したいのかを意識する事が必要。
# 通常は値の比較なので、特殊なケースでなければ == と考えていて良い。
#---------------------
#
# (1). 文字列に側値を代入すると、同一の測地を参照するので is も == も同じになる。
#
str1 = "Hello"   # str1 と str2 は同じ即値の "Hello" を指す
str2 = "Hello"

print('isで比較')
if str1 is str2:
    print(' 一致')
else:
    print(' 不一致')
print('== で比較')    
if str1==str2:
    print(' 一致')
else:
    print(' 不一致')

#
# (2). 文字列にストリングの位置など、同じ値でも違う場所を代入すると is と == で結果が異なる。
#      is では不一致になる。
#
def getStr(id):
    basestr = "HelloHello"
    if id==1:
        return basestr[0:4]
    else:
        return basestr[5:9]

str1 = getStr(1)   # 関数からの戻りが 同じ値だが位置が異なる(=同じ値の異なるオブジェクト)
str2 = getStr(2)
print('isで比較')
if str1 is str2:
    print(' 一致')
else:
    print(' 不一致')
print('==で比較')
if str1==str2:
    print(' 一致')
else:
    print(' 不一致')


# In[ ]:


#------------------------------
# in / not in
#------------------------------
# 文字列、または、リストやタプルの中に含まれるかのチェック
#   *タプル - Javaには無い。リストと似ているが変更できない点が大きな違い。
#


# In[ ]:


#................
# List/Tuple
#................


# In[9]:


# in の例 / Listで
fruits = ['バナナ', 'みかん', 'りんご']
if 'みかん' in fruits:
    print('あり')
else:
    print('なし')

# not in の例 / Tupleで
fruits_tuple = ('バナナ', 'パイナップル', 'りんご') # これがタプル。()で括る。append などはできない。
if 'みかん' not in fruits_tuple:
    print('なし')
else:
    print('あり')


# In[ ]:


#................
# 文字列
#................


# In[10]:


OnDuty = '今日は鈴木さん、小林さん、岡田さん、佐藤さん、村田さんが当番です'
if '佐藤' in OnDuty:
    print('今日の当番')
else:
    print('当番ではない')


# In[ ]:


#------------------------------
# pass
#------------------------------
# 何もしない。
# if文での条件に合致したら何もしない時などに使える。
#


# In[2]:


def checkList(val):
    fruits_tuple = ('バナナ', 'パイナップル', 'りんご')
    if val in fruits_tuple:
        return fruits_tuple[fruits_tuple.index(val)]
    else:
        return None

result = checkList('みかん')
if result is None:
    # None の場合は何も処理を行わない例。
    # ifで合致した時の処理が無いと実行エラーになるので pass を入れる。
    # ここの例ではis notで記述もでき、大差ないが、
    #   実際の実装では、何もしないケースを抽出する方がシンプルで明確な場合がしばしばあるので便利。
    pass
else:
    print(result)
    


# In[5]:


#------------------------------
# Java の else if は elif
#------------------------------
# 書き方が違うというだけの話。
chkval = 1
if chkval==0:
    print('Low')
elif chkval==1:
    print('Mid')
else:
    print('High')


# In[ ]:




