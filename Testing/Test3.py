# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:59:26 2023

@author: TomiComi
"""

import spacy
import re
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas
from __init__ import dataframeManagementClusters,dataframeManagementClusters2,dataframeManagementValue2
from __init__ import verifyText


d = {'year': [1950,1960,1970,1980],
      'value': [0,0,0,0]}

d_3 = {'Type': ["ValuePosClusters","ValueNegClusters"],
      'value': [0,0]}
df_positive_clusters = pandas.DataFrame(data=d)
df_negative_clusters = pandas.DataFrame(data=d)

df_1950_valueC=pandas.DataFrame(data=d_3)
df_1960_valueC=pandas.DataFrame(data=d_3)
df_1970_valueC=pandas.DataFrame(data=d_3)
df_1980_valueC=pandas.DataFrame(data=d_3)

df_pos_value=pandas.DataFrame(data=d)
df_neg_value=pandas.DataFrame(data=d)


List_pos_results=[];
List_neg_results=[];

nlp = spacy.load("hr_core_news_lg")

List_year= [1950,1960,1970,1980]
clusters_list=["Positive clusters","Negative clusters"]



# Definiranje uzorka uz pomoć regularnog izraza
patternpositive1=r'\"[^"]*(\w*primitiv\w*|\w*egzot\w*|\w*crn(?!\w*ač\w*)\w*|\w*treć\w* \w*svijet\w*)"[^"]*'
patternpositive2= r'(tzv\.\s|\w*takozvan\w.*?)(\w*primitiv\w*|\w*egzot\w*|\w*crn\w*|\w*treć\w* \w*svijet\w*)'


patternnegative="\b*primitiv\w*|\w*egzotič\w*|\w*crn(?!\w*ač\w*)\w*|\w*treć\w* \w*svijet\w*"







# pattern = r'tzv\.\s\w*primitiv\w*|\w*takozvan\w.*?\w*primitiv\w*|\"[^"]*\w*primitivac\w*[^"]*\"'
# pattern2 = r"\w*takozvan\w.*?\w*primitiv\w*"
# p3=r'tzv\.\s*takozvan\w.*?\w*primitiv\w*|\"[^"]*\w*primitivac\w*[^"]*\"'

#p5=r'(?:"|\')?(?:\w*t\w.*?\w*|egzoticn\w*|primitivac)\b(?:\w+\s)*(?:"|\')?'

# f = open("1960.txt", 'r',encoding="utf8")
# content = f.read()
# #print(content)
# f.close()

# doc=nlp(content)

# matches = re.findall(pattern1, doc.text)

# a=(len(matches))
# print("---------------------------------")
# for match in matches:
#         print(match)
   
    #Ispis pronađenih podudaranja
# for match in matches:
#     print(match)

for i in List_year:
    a=0
    b=0
    c=0
    result=0
    resultA=0
    resultB=0
    
    
    f = open(str(i)+".txt", 'r',encoding="utf8")
    content = f.read()
    #print(content)
    f.close()

    doc=nlp(content)
    
    matches = re.findall(pattern1, doc.text)
    print(i)
    a=(len(matches))
    print("---------------------------------")
   
    # Ispis pronađenih podudaranja
    for match in matches:
        print(match)
    
    matches = re.findall(p4, doc.text)
    b=(len(matches))
    print("---------------------------------")
    # Ispis pronađenih podudaranja
    for match in matches:
        print(match)   
    print("---------------------------------")
    
    matches = re.findall(p6, doc.text)

    c=(len(matches))
    print("---------------------------------")
       
        # Ispis pronađenih podudaranja
    for match in matches:
        print(match)
    
    
    result=a+b
   
    
    ukupno=result+c
   
        
    resultA=result/ukupno
    resultB=c/ukupno
    List_neg_results.append(c)
    List_pos_results.append(result)
    print("ukupno:",result)
    print("---------------------------------")
    
    dataframeManagementClusters(df_positive_clusters,df_negative_clusters,i,resultA,resultB)
    if(i==1950):
        dataframeManagementClusters2(df_1950_valueC, i, result,c)
        df_pos_value.loc[df_pos_value["year"]== 1950,"value"]=c
        df_neg_value.loc[df_neg_value["year"]== 1950,"value"]=result
    elif(i==1960):
        dataframeManagementClusters2(df_1960_valueC, i, result,c)
    elif(i==1970):
        dataframeManagementClusters2(df_1970_valueC, i, result,c)
    else:
        dataframeManagementClusters2(df_1980_valueC, i,  result,c)
        
    dataframeManagementValue2(df_pos_value,i,c)
    dataframeManagementValue2(df_neg_value,i,result)    
    
    print("zavrseno")


# dataframeManagementValue2(df_pos_value,i,List_pos_results)
# dataframeManagementValue2(df_neg_value,i,List_neg_results)
# print(List_pos_results,"je positivno ",List_neg_results,"je negativno")
# print("df su:",df_positive_clusters,df_negative_clusters)
print("novo")
print(df_pos_value,df_neg_value)

# plt.figure(9)

# # bar_labels = ['1950', '1960', '1970', '1980']

# plt.plot(df_positive_clusters['year'], df_positive_clusters['value'],color='tab:green', 
#                                                                       alpha=1,label = "1950", linewidth = '5')
# plt.plot(df_negative_clusters['year'], df_negative_clusters['value'],color='tab:red',
#                                                                              alpha=1,label = "1960", linewidth = '5')

# plt.xlabel('Decades')
# plt.ylabel('Presence value in %')
# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
# plt.title("Word Relations 1950-1980",fontweight='bold')
# plt.legend(title='Year')


# plt.figure(7)

# fig, axs = plt.subplots(2, 2)
# axs[0,0].pie(df_1950_valueC['value'], autopct='%1.1f%%',labels=clusters_list,shadow=True,
#                                                                              startangle=90,explode=[0.1,0])
# axs[0,0].set_title("Word Relations 1950",fontweight='bold')
  
# axs[0,0].legend(
#       title="Word Types",
#       loc="center left",
#       bbox_to_anchor=(1, 0, 0.5, 1))

# axs[0,1].pie(df_1960_valueC['value'], autopct='%1.1f%%',labels=clusters_list,shadow=True,
#                                                                              startangle=90,explode=[0.1,0])
# axs[0,1].set_title("Word Relations 1960",fontweight='bold')
  
# axs[0,1].legend(
#       title="Word Types",
#       loc="center left",
#       bbox_to_anchor=(1, 0, 0.5, 1))

# axs[1,0].pie(df_1970_valueC['value'], autopct='%1.1f%%',labels=clusters_list,shadow=True,
#                                                                             startangle=90,explode=[0.1,0])
# axs[1,0].set_title("Word Relations 1970",fontweight='bold')
# axs[1,0].legend(
#       title="Word Types",
#       loc="center left",
#       bbox_to_anchor=(1, 0, 0.5, 1))

# axs[1,1].pie(df_1980_valueC['value'], autopct='%1.1f%%',labels=clusters_list,shadow=True,
#                                                                             startangle=90,explode=[0,0.1])
# axs[1,1].set_title("Word Relations 1980",fontweight='bold')
# axs[1,1].legend(
#       title="Word Types",
#       loc="center left",
#       bbox_to_anchor=(1, 0, 0.5, 1))



  
# fig, ax = plt.subplots()
# #counts, edges, bars = .hist([df_1980_valueC['value'], df_1960_valueC['value'] * 0.3], histtype='barstacked')
# counts, edges, bars = df_pos_value['value'].hist()
# for b in bars:
#     ax.bar_label(b)


# df = pandas.DataFrame({

#     'length': [1950,1960,1970,1980],

#     'width': [df_1950_valueC['value'][1], df_1960_valueC['value'][1], df_1970_valueC['value'][1], df_1980_valueC['value'][1]]

#     }, index=['pig', 'rabbit', 'duck', 'chicken'])

# hist = df.hist(bins=3)


# y1 = [df_1950_valueC['value'][1], df_1960_valueC['value'][1], df_1970_valueC['value'][1], df_1980_valueC['value'][1]]
# y2 = [df_1950_valueC['value'][0], df_1960_valueC['value'][0], df_1970_valueC['value'][0], df_1980_valueC['value'][0]]
# colors = ['b','g']

# #plots the histogram
# fig, ax1 = plt.subplots()
# ax1.hist([y1,y2],color=colors)
# ax1.set_xlim(0,30)
# ax1.set_ylabel("Count")
# plt.tight_layout()
# plt.show()
  
# generate some example data as a Pandas DataFrame
# generate some example data as a Pandas DataFrame
# years = pandas.date_range('2000-01-01', '2022-12-31', freq='Y')
# years = [1950,1960,1970,1980]
# pos_values = pandas.Series(data=[df_1950_valueC['value'][1], df_1960_valueC['value'][1], df_1970_valueC['value'][1], df_1980_valueC['value'][1]], index=years)
# neg_values = pandas.Series(data=[df_1950_valueC['value'][0], df_1960_valueC['value'][0], df_1970_valueC['value'][0], df_1980_valueC['value'][0]], index=years)
# data = pandas.DataFrame({'years': years, 'pos_values': pos_values, 'neg_values': neg_values})

# # create the figure and axes objects
# fig, ax = plt.subplots()

# # create the stacked histogram
# ax.hist([data['years'], data['years']], bins=len(years), weights=[data['pos_values'], data['neg_values']], stacked=True)

# # set the x-axis labels and tick marks
# ax.set_xticks(pandas.to_datetime(['1950-01-01', '1960-01-01', '1970-01-01', '1980-01-01']))
# ax.set_xticklabels(['1950', '1960', '1970', '1980'], rotation=90)

# # set the axis labels and title
# ax.set_xlabel('Year')
# ax.set_ylabel('Value')
# ax.set_title('Stacked Histogram of Positive and Negative Values by Year')

# # add a legend
# ax.legend(['Positive Values', 'Negative Values'])

# # add grid lines
# ax.grid(axis='y', linestyle='--')

# # adjust the layout and padding
# fig.tight_layout(pad=2)
# # show the plot
# plt.show()

# create a pandas dataframe with years and values
data = {'Year': ['1950', '1960', '1970', '1980'],
        'Positive Values':List_pos_results,
        'Negative Values': List_neg_results}
df = pandas.DataFrame(data)

# create variables for positive and negative values
positive = df['Positive Values']
negative = df['Negative Values']

# create bar graph with positive and negative values
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(df['Year'], positive, color='blue', label='Positive', alpha=0.7, edgecolor='black', linewidth=1.5)
ax.bar(df['Year'], negative, color='orange', label='Negative', alpha=0.7, edgecolor='black', linewidth=1.5, bottom=positive)

# add labels and title to the graph
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Value', fontsize=14)
ax.set_title('Positive and Negative Values by Year', fontsize=16, fontweight='bold')

# add legend to the graph
ax.legend(fontsize=12, loc='upper left')

# add grid lines to the graph
ax.grid(axis='y', linestyle='--', alpha=0.7)

# add text labels to the bars
for i, v in enumerate(positive):
    ax.text(i, v/2, str(v), ha='center', va='center', color='white', fontsize=12)
for i, v in enumerate(negative):
    ax.text(i, v/2, str(v), ha='center', va='center', color='white', fontsize=12)

# adjust layout of the graph
fig.tight_layout()

# save the graph as a PNG file
plt.savefig('positive_negative_values.png')

# show the graph
plt.show()