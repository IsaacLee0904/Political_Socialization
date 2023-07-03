''' Online_PP and Offline_PP '''
# news_time 
def news_time(x):
    if x == '30分鐘以下':
        return float(1)
    elif x == '30-60分鐘':
        return float(2)
    elif x == '60-90分鐘':
        return float(3)
    elif x == '90-120分鐘':
        return float(4)
    else:
        return float(5)

# TV_debate 
def TV_debate(x):
    if x == '非常不符合':
        return float(1)
    elif x == '不太符合':
        return float(2)
    elif x == '還算符合':
        return float(3)
    elif x == '非常符合':
        return float(4)
    else:
        return float('NaN')

# read_media 
def read_media(x):
    if x == '從來不瀏覽':
        return float(1)
    elif x == '很少瀏覽':
        return float(2)
    elif x == '有時瀏覽':
        return float(3)
    elif x == '時常瀏覽':
        return float(4)
    else:
        return float('NaN')

# like_media
def like_media(x):
    if x == '從來不按讚':
        return float(1)
    elif x == '很少按讚':
        return float(2)
    elif x == '有時按讚':
        return float(3)
    elif x == '時常按讚':
        return float(4)
    else:
        return float('NaN')

# share_media
def share_media(x):
    if x == '從來不分享':
        return float(1)
    elif x == '很少分享':
        return float(2)
    elif x == '有時分享':
        return float(3)
    elif x == '時常分享':
        return float(4)
    else:
        return float('NaN')

# comment_media
def comment_media(x):
    if x == '從來不留言':
        return float(1)
    elif x == '很少留言':
        return float(2)
    elif x == '偶爾留言':
        return float(3)
    elif x == '時常留言':
        return float(4)
    else:
        return float('NaN')

# int_discuss
def int_discuss(x):
    if x == '從來不討論':
        return float(1)
    elif x == '很少討論':
        return float(2)
    elif x == '有時討論':
        return float(3)
    elif x == '時常討論':
        return float(4)
    else:
        return float('NaN')

# read_election_news & read_election_leaflet & campaign & volunteer
def Likert(x):
    if x == '非常不符合':
        return float(1)
    elif x == '不太符合':
        return float(2)
    elif x == '還算符合':
        return float(3)
    elif x == '非常符合':
        return float(4)
    else:
        return float('NaN')

# convince 
def convince(x):
    if x == '從來不勸說':
        return float(1)
    elif x == '很少勸說':
        return float(2)
    elif x == '有時勸說':
        return float(3)
    elif x == '時常勸說':
        return float(4)
    else:
        return float('NaN')

# election_mayor & election_18
def election(x):
    if x == '非常不可能':
        return float(1)
    elif x == '不太有可能':
        return float(2)
    elif x == '還算有可能 ':
        return float(3)
    elif x == '非常有可能':
        return float(4)
    else:
        return float('NaN')

''' Demographic variables '''
# sex
def sex(x):
    if x == '男性':
        return int(1)
    elif x == '女性':
        return int(0)
    else:
        return float('NaN')

# age
def age(x):
    if x == '20-29歲':
        return int(1)
    elif x == '30-39歲':
        return int(2)
    elif x == '40-49歲':
        return int(3)    
    elif x == '50-59歲':
        return int(4)     
    elif x == '60歲以上':
        return int(5) 
    else:
        return float('NaN')
      
# ethnic
def ethnic(x):
    if isinstance(x, float):  # check if x is a float
        x = str(x)  # convert x to string if it is a float

    if '本省閩南人' in x:
        return str('本省閩南人') # 本省閩南人
    elif '本省客家人' in x:
        return str('本省客家人') # 本省客家人
    elif '大陸各省市人' in x: 
        return str('大陸各省市人') # 大陸各省市人 
    elif '原住民' in x:
        return str('原住民') # 原住民    
    elif '台灣人' in x or '臺灣人' in x:
        return str('臺灣人') # 台灣人
    else:
        return str('其他') # 其他
      
# edu
def edu(x):
    if x == '國中':
        return int(1)
    elif x == '高中（職）':
        return int(2)
    elif x == '大專（學）':
        return int(3)    
    elif x == '研究所以上':
        return int(4)     
    else:
        return float('NaN')
      
# income
def income(x):
    if x == '無收入(例如:為家庭事業工作，但沒有領薪水)':
    	return int(1)
    elif x == '2萬元以下':
    	return int(2)
    elif x == '2-4 萬元':
    	return int(3)
    elif x == '4-6 萬元':
    	return int(4)
    elif x == '6-8萬元':
    	return int(5)
    elif x == '8-10 萬元':
    	return int(6)
    elif x == '10-15 萬元':
    	return int(7)
    elif x == '15-20 萬元':
    	return int(8)
    elif x == '20萬以上':
    	return int(9)
    else:
    	return float('NaN')

# Political knowledge
def pk_1(x):
  if x == '拜登':
    return int(1)
  else:
    return int(0)
  
def pk_2(x):
  if x == '蘇貞昌':
    return int(1)
  else:
    return int(0)
  
def pk_3(x):
  if x == '司法院':
    return int(1)
  else:
    return int(0)

# for Anti Party Sentiment & TW and China issue
def five_agree(x):
  if x == '非常同意':
    return int(5)
  if x == '還算同意':
    return int(4)
  if x == '沒有意見':
    return int (3)
  if x == '不太同意':
    return int(2)
  if x == '非常不同意':
    return int(1)
  else:
    return float('NaN')
    
    