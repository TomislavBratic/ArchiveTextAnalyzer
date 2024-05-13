# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:14:35 2023

@author: TomiComi
"""

import spacy
from VerificationLists.Lists import text_neg_adj,text_neg_clusters,text_neg_nouns,text_pos_adj,text_pos_clusters,text_pos_nouns

def verifyText(filename):
    nlp = spacy.load("hr_core_news_lg")
    f = open(filename, 'r',encoding="utf8")
    content = f.read()
    #print(content)
    f.close()


    doc=nlp(content.lower())
    List_neg_adj=[]
    List_main_text=[]
    List_pos_adj=[]
    List_neg_nouns=[]
    List_pos_nouns=[]
    List_pos_clusters=[]
    List_neg_clusters=[]
    counter_negative_adj=0;
    counter_positive_adj=0;
    counter_negative_nouns=0;
    counter_positive_nouns=0;
    counter_positive_clusters=0;
    counter_negative_clusters=0;
    List_information=[];
    textNumberOfWords=len(content)
    
  
    doc_negative_adj=nlp(text_neg_adj.lower())
    doc_positive_adj=nlp(text_pos_adj.lower())
    doc_negative_nouns=nlp(text_neg_nouns.lower())
    doc_positive_nouns=nlp(text_pos_nouns.lower())
    doc_negative_clusters=nlp(text_neg_clusters.lower())
    doc_positive_clusters=nlp(text_pos_clusters.lower())
  
    
    text_clear_neg_adj=[token for token in doc_negative_adj if not token.is_punct and not token.is_stop]
    ' '.join(token.text for token in text_clear_neg_adj)
    text_clear_main_text=[token for token in doc if not token.is_punct and not token.is_stop]
    ' '.join(token.text for token in text_clear_main_text)
    text_clear_pos_adj=[token for token in doc_positive_adj if not token.is_punct and not token.is_stop]
    ' '.join(token.text for token in text_clear_pos_adj)
    text_clear_neg_nouns=[token for token in doc_negative_nouns if not token.is_punct and not token.is_stop]
    ' '.join(token.text for token in text_clear_neg_nouns)
    text_clear_pos_nouns=[token for token in doc_positive_nouns if not token.is_punct and not token.is_stop]
    ' '.join(token.text for token in text_clear_pos_nouns)
    text_clear_neg_clusters=[token for token in doc_negative_clusters if not token.is_punct and not token.is_stop]
    ' '.join(token.text for token in text_clear_neg_clusters)
    text_clear_pos_clusters=[token for token in doc_positive_clusters if not token.is_punct and not token.is_stop]
    ' '.join(token.text for token in text_clear_pos_clusters)



    for token in text_clear_neg_adj:
        List_neg_adj.append(str(token))
        
    for token in text_clear_main_text:
        List_main_text.append(str(token))
        
    for token in text_clear_pos_adj:
        List_pos_adj.append(str(token)) 
    
    for token in text_clear_neg_nouns:
        List_neg_nouns.append(str(token))  
    
    for token in text_clear_pos_nouns:
        List_pos_nouns.append(str(token)) 
         
    for token in text_clear_pos_clusters:
        List_pos_clusters.append(str(token))   
    
    for token in text_clear_neg_clusters:
        List_neg_clusters.append(str(token))    

     

#List1=["civilizacija","egzotično"...]    

#for word in List1:    
 #print(word)
#for word in List2:    
  #print(word) 
    for word in List_neg_adj:
      if word in List_main_text:
              #print("Pridjevi koji su negativni:",word)
              counter_negative_adj=counter_negative_adj+1
    print("--------------------------")
    for word in List_pos_adj:
      if word in List_main_text:
              #print("Pridjevi koji su pozitivni:",word)
              counter_positive_adj=counter_positive_adj+1
        
    print("-----------------------------")
    for word in List_neg_nouns:
      if word in List_main_text:
              #print("Imenice koje su negativne:",word)
              counter_negative_nouns=counter_negative_nouns+1

    print("-----------------------------")
    for word in List_pos_nouns:
      if word in List_main_text:
              #print("Imenice koje su pozitivne:",word)
              counter_positive_nouns=counter_positive_nouns+1
              
    print("positive clusters:")          
    for i in range(0,len(List_pos_clusters),2):
         try:
             for j in range(0,len(List_main_text),2):
                 try:
                     if(List_pos_clusters[i]==List_main_text[j] and List_pos_clusters[i+1]==List_main_text[j+1]):
                        
                         print(List_pos_clusters[i],List_pos_clusters[i+1])
                         counter_positive_clusters=counter_positive_clusters+1
                         
                    
                 except IndexError:
                    List_main_text[j]="null"           
            
         except IndexError:
            List_pos_clusters[i]="null"
              
    print("-----------------------------")          
    print("negative clusters:")          
    for i in range(0,len(List_neg_clusters),2):
        try:
            for j in range(0,len(List_main_text),2):
                try:
                    if(List_neg_clusters[i]==List_main_text[j] and List_neg_clusters[i+1]==List_main_text[j+1]):
                      
                        print(List_neg_clusters[i],List_neg_clusters[i+1])
                        counter_negative_clusters=counter_negative_clusters+1
                   
                except IndexError:
                   List_main_text[j]="null"           
           
        except IndexError:
           List_neg_clusters[i]="null"
           
    print("-----------------------------")               
        
      # if word2 in List_main_text:
      #          #print("Imenice koje su pozitivne:",word)
      #          counter_negative_clusters=counter_negative_clusters+1  
      #          print(word1,"je prva",word2,"je druga")
  

    sum1=counter_positive_adj+counter_negative_adj+counter_positive_nouns+counter_negative_nouns
    sumclusters=counter_positive_clusters+counter_negative_clusters
    # sum_positive=counter_positive_adj+counter_positive_nouns
    # sum_negative=counter_negative_adj+counter_negative_nouns

    # print("Postotak pozitivnih pridjeva:",(counter_positive_adj/sum)*100,"%")
    # print("Postotak negativnih pridjeva:",(counter_negative_adj/sum)*100,"%")
    # print("Postotak pozitivnih imenica:",(counter_positive_nouns/sum)*100,"%")
    # print("Postotak negativnih imenuca:",(counter_negative_nouns/sum)*100,"%")
    # print("-----------------------------")
    

    # print("Postotak negativnih rijeci:",((counter_negative_nouns+counter_negative_adj)/sum)*100,"%")
    # print("Postotak pozitivnih rijeci:",((counter_positive_nouns+counter_positive_adj)/sum)*100,"%")
    
    
    if(sum1==0):
         sum1=1
    if(sumclusters==0):
         sumclusters=1
    # List_information.append((sum_positive/sum1)*100)
    # List_information.append((sum_negative/sum1)*100)
    
    print("Ucitavanje:0%")
    List_information.append((counter_positive_adj/sum1)*100)
    print("Ucitavanje:25%")
    List_information.append((counter_negative_adj/sum1)*100)
    print("Ucitavanje:50%")
    List_information.append((counter_positive_nouns/sum1)*100)
    print("Ucitavanje:75%")
    List_information.append((counter_negative_nouns/sum1)*100)
    print("Ucitavanje:100%")
    List_information.append((counter_positive_clusters/sumclusters)*100)
    print("Ucitavanje:100%")
    List_information.append((counter_negative_clusters/sumclusters)*100)
    print("Ucitavanje:100%")
    
    
    # List_information.append((counter_positive_adj))
    # List_information.append((counter_negative_adj))
    # List_information.append((counter_positive_nouns))
    # List_information.append((counter_negative_nouns))
    
    if(len(List_information)==6):
        return List_information
    else:
        print("greska u slanju")






