## Import package
# for data ETL
import pandas as pd
import numpy as np
import ETL_function


def data_cleaning(filter_data):  
  
  ''' DV '''
  filter_data['TV_news_time'] = filter_data['請問您平均每天花多少時間注意電視上的選舉新聞？'].apply(ETL_function.news_time)
  filter_data['news_paper_time'] = filter_data['請問您平均每天花多少時間注意報紙上的選舉新聞？'].apply(ETL_function.news_time)
  filter_data['int_news_time'] = filter_data['請問您平均每天花多少時間注意網路上的選舉新聞？'].apply(ETL_function.news_time)
  filter_data['TV_debate'] = filter_data['今年九合一選舉中，我有觀看候選人電視辯論會。'].apply(ETL_function.TV_debate)
  filter_data['read_media'] = filter_data['請問您有多常瀏覽候選人的社群媒體？'].apply(ETL_function.read_media)
  filter_data['like_media'] = filter_data['請問您有多常在候選人的社群媒體貼文下按讚（任何表情符號）？'].apply(ETL_function.like_media)
  filter_data['share_media'] = filter_data['請問您有多常分享候選人的社群媒體貼文？'].apply(ETL_function.share_media)
  filter_data['comment_media'] = filter_data['請問您有多常在候選人的社群媒體貼文底下留言？'].apply(ETL_function.comment_media)
  filter_data['int_discuss'] = filter_data['請問您平時會不會在網路上與他人討論有關政治或選舉方面的議題？'].apply(ETL_function.int_discuss)
  filter_data['read_election_news'] = filter_data['今年九合一選舉中，我有閱讀選舉公報。'].apply(ETL_function.Likert)
  filter_data['read_election_leaflet'] = filter_data['今年九合一選舉中，我有閱讀候選人傳單、快報或報刊廣告。'].apply(ETL_function.Likert)
  filter_data['convince'] = filter_data['請問您有多常遊說或勸說親友投票給某位候選人？'].apply(ETL_function.convince)
  filter_data['campaign'] = filter_data['今年九合一選舉中，我有主動參加造勢活動。'].apply(ETL_function.Likert)
  filter_data['volunteer'] = filter_data['今年九合一選舉中，我有擔任候選人或政黨的助選工作人員或義工。'].apply(ETL_function.Likert)
  filter_data['election_mayor'] = filter_data['請問今年縣市長選舉中，您是否可能去投票？'].apply(ETL_function.election)
  filter_data['election_18'] = filter_data['請問今年18歲公民權修憲公投，您是否可能去投票？'].apply(ETL_function.election)

  ''' IV '''
  filter_data['sex'] = filter_data['受訪者性別'].apply(ETL_function.sex)
  filter_data['台灣社會有多重的身份認同，有人認為自己是本省客家人、本省閩南人、大陸各省市人或原住民，請問您認為您的認同較接近哪一個?'] = filter_data.apply(lambda row: row['其他.6'] if row['台灣社會有多重的身份認同，有人認為自己是本省客家人、本省閩南人、大陸各省市人或原住民，請問您認為您的認同較接近哪一個?'] == '其他' else row['台灣社會有多重的身份認同，有人認為自己是本省客家人、本省閩南人、大陸各省市人或原住民，請問您認為您的認同較接近哪一個?'],axis=1)
  filter_data['ethnic'] = filter_data['台灣社會有多重的身份認同，有人認為自己是本省客家人、本省閩南人、大陸各省市人或原住民，請問您認為您的認同較接近哪一個?'].apply(ETL_function.ethnic)
  filter_data['edu'] = filter_data['請問您的教育程度是什麼？'].apply(ETL_function.edu)
  filter_data['income'] = filter_data['請問您平均月收入大約是多少?'].apply(ETL_function.income)
  filter_data['pk_1'] = filter_data['請問您現任的美國總統是誰？'].apply(ETL_function.pk_1)
  filter_data['pk_2'] = filter_data['請問您現任的行政院長是誰？'].apply(ETL_function.pk_2)
  filter_data['pk_3'] = filter_data['請問您我國哪一個政府機關有權解釋憲法？'].apply(ETL_function.pk_3)
  filter_data['political_knowledge'] = filter_data['pk_1'] + filter_data['pk_2'] + filter_data['pk_3']
  anti_party_columns = ['您是否同意台灣民眾討厭國民黨及民進黨的比例，正在逐年上升中？', '有人說：「為了勝選，無論那一個政黨都會利用機會影響選舉的公平性」，請問您同不同意這種說法？', '有人說：「現在無論那一個政黨執政，都不可能把國家治理好」，請問您同不同意這種說法？', '有人說：「政黨總是相互批評，但實際上它們並無差別」，請問您同不同意這種說法？', '有人說：「政黨只會讓社會分裂？」，請問您同不同意這種說法？']
  for j, i in enumerate(anti_party_columns, 1):  # enumerate starts at 1 instead of 0
      filter_data['anti_'+str(j)] = filter_data[i].apply(ETL_function.five_agree)
  filter_data['TC_issue'] = filter_data['有人說：「這次選舉中，抗中保台很重要」，請問您同不同意這種說法？'].apply(ETL_function.five_agree)
  filter_data['Negative_1'] = filter_data['在這次縣市長選舉過程中，有大量關於林智堅的論文爭議的報導，請問這些報導對您的投票選擇可能有什麼影響？']
  filter_data['Negative_2'] = filter_data['在這次縣市長選舉過程中，有大量關於陳時中的防疫表現的報導，這些報導對您的投票選擇可能有什麼影響？']
  filter_data['Negative_3'] = filter_data['在這次縣市長選舉過程中，有大量關於高虹安的助理門事件爭議的報導，這些報導對您的投票選擇有什麼影響？']
  
  ''' reshape data frame '''
  ml_df = filter_data.loc[:, ['TV_news_time', 'news_paper_time',
         'int_news_time', 'TV_debate', 'read_media', 'like_media', 'share_media',
       'comment_media', 'int_discuss', 'read_election_news',
       'read_election_leaflet', 'convince', 'campaign', 'volunteer',
       'election_mayor', 'election_18', 'sex', 'ethnic', 'edu', 'income',
       'pk_1', 'pk_2', 'pk_3', 'political_knowledge', 'anti_1', 'anti_2',
       'anti_3', 'anti_4', 'anti_5', 'TC_issue', 'Negative_1', 'Negative_2',
       'Negative_3']]
  ml_df = ml_df.dropna()

  return ml_df

def feature_engineering(ml_df):
  ''' filiter vars by category base on reference '''
  online_pp_vars = ['TV_news_time', 'news_paper_time', 'int_news_time', 'TV_debate',     'read_media', 'like_media', 'share_media', 'comment_media', 'int_discuss']
  offline_pp_vars = ['read_election_news', 'read_election_leaflet', 'convince', 'campaign', 'volunteer', 'election_mayor', 'election_18']
  anti_party_vars = ['anti_1', 'anti_2', 'anti_3', 'anti_4', 'anti_5']

  ''' create new feature '''
  # Basic
  ml_df['online_pp'] = ml_df[online_pp_vars].mean(axis=1)
  ml_df['offline_pp'] = ml_df[offline_pp_vars].mean(axis=1)
  ml_df['anti_party'] = ml_df[anti_party_vars].mean(axis=1)
  
  return ml_df
 
  
def anti_party_feature(ml_df):
  
  # anti_party index 
  ## 因素分析 -> 根據構面取平均
  political_polarization_vars = ['anti_1']
  party_image_vars = ['anti_3', 'anti_4', 'anti_5']
  ml_df['political_polarization_mean'] = ml_df[political_polarization_vars].mean(axis=1)
  ml_df['party_image_mean'] = ml_df[party_image_vars].mean(axis=1)
  ## 因素分析 -> 根據構面取綜合得分
  ## 因素分析 -> 全部算一個綜合得分
  
  return ml_df