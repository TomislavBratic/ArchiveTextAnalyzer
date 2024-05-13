# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import spacy
from spacy import displacy
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas
from __init__ import dataframeManagement,dataframeManagementSum,dataframeManagementValue
from __init__ import verifyText




def main():
    
    List_year= [1950,1960,1970,1980]
    
    
    print("---------------------------------------------------")
    d = {'year': [1950,1960,1970,1980],
         'value': [0,0,0,0]}
    
    d_2 = {'Type': ["ValuePosAdj","ValueNegAdj","ValuePosNouns","ValueNegNouns"],
         'value': [0,0,0,0]}
    d_3 = {'Type': ["ValuePosClusters","ValueNegClusters"],
         'value': [0,0]}
    
    df_positive_adjectives = pandas.DataFrame(data=d)
    df_negative_adjectives=pandas.DataFrame(data=d)
    df_positive_nouns=pandas.DataFrame(data=d)
    df_negative_nouns=pandas.DataFrame(data=d)
    
    df_1950_value=pandas.DataFrame(data=d_2)
    df_1960_value=pandas.DataFrame(data=d_2)
    df_1970_value=pandas.DataFrame(data=d_2)
    df_1980_value=pandas.DataFrame(data=d_2)
    
    df_1950_valueC=pandas.DataFrame(data=d_3)
    df_1960_valueC=pandas.DataFrame(data=d_3)
    df_1970_valueC=pandas.DataFrame(data=d_3)
    df_1980_valueC=pandas.DataFrame(data=d_3)
    # df_positive = pandas.DataFrame(data=d)
    # df_negative= pandas.DataFrame(data=d)
    
  
    
    List_information=[]
    
   
    for yearNumber in List_year:
         file=str(yearNumber)+".txt"
         
         print("Ucitavanje godine:",yearNumber)
         List_information=verifyText(file)
         print("zavrseno")
         print("Dataframe Management:")
         #dataframeManagementSum(df_positive, df_negative, yearNumber, List_information)
         dataframeManagement(df_positive_adjectives, df_negative_adjectives, df_positive_nouns, df_negative_nouns, yearNumber, List_information)
         if(yearNumber==1950):
             dataframeManagementValue(df_1950_value,df_1950_valueC, yearNumber, List_information)
         elif(yearNumber==1960):
             dataframeManagementValue(df_1960_value,df_1960_valueC, yearNumber, List_information)
         elif(yearNumber==1970):
             dataframeManagementValue(df_1970_value,df_1970_valueC, yearNumber, List_information)
         else:
             dataframeManagementValue(df_1980_value,df_1980_valueC, yearNumber, List_information)      
         print("zavrseno")
   
         
   
    # print("positive adjectives:")
    # print(df_positive_adjectives)
    # print("---------------------------")
    # print(" negative adjectives:")
    # print(df_negative_adjectives)
    # print("---------------------------")
    # print("positive nouns:")
    # print(df_positive_nouns)
    # print("---------------------------")
    # print("negative nouns:")
    # print(df_negative_nouns)
    # print("---------------------------")
          
    print("positive adjectives:")
    print(df_1950_value)
    print("---------------------------")
    print(" negative adjectives:")
    print(df_1960_value)
    print("---------------------------")
    print("positive nouns:")
    print(df_1970_value)
    print("---------------------------")
    print("negative nouns:")
    print(df_1980_value)
    print("---------------------------")
    
    plt.figure(3)
    
    # bar_labels = ['1950', '1960', '1970', '1980']

    plt.plot(df_positive_adjectives['year'], df_positive_adjectives['value'],color='tab:green', 
                                                                          alpha=1,label = "1950", linewidth = '5')
    plt.plot(df_negative_adjectives['year'], df_negative_adjectives['value'],color='tab:red',
                                                                                 alpha=1,label = "1960", linewidth = '5')
    plt.plot(df_positive_nouns['year'], df_positive_nouns['value'],color='tab:blue', 
                                                                               alpha=1,label = "1970", linewidth = '5')
    plt.plot(df_negative_nouns['year'], df_negative_nouns['value'],color='tab:orange', 
                                                                               alpha=1,label = "1980", linewidth = '5')
    plt.xlabel('Decades')
    plt.ylabel('Presence value in %')
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    plt.title("Word Relations 1950-1980",fontweight='bold')
    plt.legend(title='Year')
   
 
    plt.figure(4)
    word_labels=["Positive adjectives","Negative adjectives","Positive nouns","Negative nouns"]
    clusters_list=["Positive clusters","Negative clusters"]
    
    fig, axs = plt.subplots(2, 2)
    axs[0,0].pie(df_1950_value['value'], autopct='%1.1f%%',labels=word_labels,shadow=True,
                                                                                startangle=90,explode=[0.1,0,0,0])
    axs[0,0].set_title("Word Relations 1950",fontweight='bold')
      
    axs[0,0].legend(
          title="Word Types",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
    
    axs[0,1].pie(df_1960_value['value'], autopct='%1.1f%%',labels=word_labels,shadow=True,
                                                                                startangle=90,explode=[0,0.1,0,0])
    axs[0,1].set_title("Word Relations 1960",fontweight='bold')
      
    axs[0,1].legend(
          title="Word Types",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
    
    axs[1,0].pie(df_1970_value['value'], autopct='%1.1f%%',labels=word_labels,shadow=True,
                                                                                startangle=90,explode=[0,0,0.1,0])
    axs[1,0].set_title("Word Relations 1970",fontweight='bold')
    axs[1,0].legend(
          title="Word Types",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
    
    axs[1,1].pie(df_1980_value['value'], autopct='%1.1f%%',labels=word_labels,shadow=True,
                                                                                startangle=90,explode=[0,0,0,0.1])
    axs[1,1].set_title("Word Relations 1980",fontweight='bold')
    axs[1,1].legend(
          title="Word Types",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

    
    
    
    
    plt.figure(5)
   
    fig, axs = plt.subplots(2, 2)
    axs[0,0].pie(df_1950_valueC['value'], autopct='%1.1f%%',labels=clusters_list,shadow=True,
                                                                                 startangle=90,explode=[0.1,0])
    axs[0,0].set_title("Word Relations 1950",fontweight='bold')
      
    axs[0,0].legend(
          title="Word Types",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
    
    axs[0,1].pie(df_1960_valueC['value'], autopct='%1.1f%%',labels=clusters_list,shadow=True,
                                                                                 startangle=90,explode=[0.1,0])
    axs[0,1].set_title("Word Relations 1960",fontweight='bold')
      
    axs[0,1].legend(
          title="Word Types",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
    
    axs[1,0].pie(df_1970_valueC['value'], autopct='%1.1f%%',labels=clusters_list,shadow=True,
                                                                                startangle=90,explode=[0.1,0])
    axs[1,0].set_title("Word Relations 1970",fontweight='bold')
    axs[1,0].legend(
          title="Word Types",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
    
    axs[1,1].pie(df_1980_valueC['value'], autopct='%1.1f%%',labels=clusters_list,shadow=True,
                                                                                startangle=90,explode=[0,0.1])
    axs[1,1].set_title("Word Relations 1980",fontweight='bold')
    axs[1,1].legend(
          title="Word Types",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.show()
 
   
    
    
   
    
    
    
  
   
    # axs[0,0].set_title("Word Relations,1950-1980")
    # axs[0,0].set_xlabel("Decades")
    # axs[0,0].set_ylabel("Presence value in %")
    # axs[0,1,1].set_title('Axis [1, 1]')
    # axs[1,0,0].plot(x, -y, 'tab:red')
    # axs[1,0,0].set_title('Axis [1, 1]')
    # axs[1,0,1].plot(x, -y, 'tab:red')
    # axs[1,0,1].set_title('Axis [1, 1]')
    # axs[1,1,0].plot(x, -y, 'tab:red')
    # axs[1,1,0].set_title('Axis [1, 1]')
    # axs[1,1,1].plot(x, -y, 'tab:red')
    # axs[1,1,1].set_title('Axis [1, 1]')


# Hide x labels and tick labels for top plots and y ticks for right plots.
  
          
        
    # fig, axs = plt.subplots(2, 2)
    # axs[0, 0].plot(df_positive_adjectives['year'], df_positive_adjectives['value'],color='green', 
    #                                                                              alpha=1,label = "Values in %")
    # axs[0, 0].plot(df_negative_adjectives['year'], df_negative_adjectives['value'],color='red',
    #                                                                              alpha=1, label = "positive adjeciives") 
    # axs[0, 0].plot(df_positive_nouns['year'], df_positive_nouns['value'],color='blue', 
    #                                                                              alpha=1,label = "positive nouns")
    # axs[0, 0].plot( df_negative_nouns['year'], df_negative_nouns['value'],color='black',
    #                                                                              alpha=1,label = "negative nouns")
    # axs[0, 0].set_title("Word Relation,1950-1980")
    # axs[1, 0].pie(df_1950_value['value'], autopct='%1.1f%%',labels=df_1950_value["Type"],shadow=True,
    #                                                                              startangle=90,explode=[0.1,0,0,0])
    # axs[1, 0].pie('equal')
    # axs[1, 0].set_title('Word Relations 1950')
    # axs[1, 0].sharex(axs[0, 0])
    
    # axs[0, 1].pie(df_1960_value['value'], autopct='%1.1f%%',labels=df_1960_value["Type"],shadow=True,
    #                                                                               startangle=90,explode=[0.1,0,0,0])
    # axs[0, 1].pie('equal')
    # axs[0, 1].set_title('Word Relations 1960')
    
    # axs[1, 1].pie(df_1970_value['value'], autopct='%1.1f%%',labels=df_1970_value["Type"],shadow=True,
    #                                                                               startangle=90,explode=[0.1,0,0,0])
    # axs[1, 1].pie('equal')
    # axs[1, 1].set_title('Word Relations 1970')
    # fig.tight_layout()
    

    
    # plt.plot(df_positive_adjectives['year'], df_positive_adjectives['value'],color='green', 
    #                                                                   alpha=1,label = "Values in %")
    
    
    # plt.plot(df_negative_adjectives['year'], df_negative_adjectives['value'],color='red', alpha=1, label = "positive adjeciives")
    
    
    # plt.plot(df_positive_nouns['year'], df_positive_nouns['value'],color='blue', alpha=1,
    #            label = "positive nouns")

    
    # plt.plot(df_negative_nouns['year'], df_negative_nouns['value'],color='black', alpha=1,
    #          label = "negative nouns")
    
    
    
    # # plt.plot(df_positive['year'], df_positive['value'],color='green', 
    # #                                                               alpha=1,label = "positive")
    # # plt.plot(df_negative['year'], df_negative['value'],color='red', 
    # #                                                               alpha=1,label = "positive")
   
    # plt.pie(df_1950_value['value'], autopct='%1.1f%%',labels=df_1950_value["Type"],shadow=True, startangle=90,explode=[0.1,0,0,0])
    # plt.title('Word Relations 1950')
    # plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    main()

