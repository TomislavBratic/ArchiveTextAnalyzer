# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:02:46 2023

@author: TomiComi
"""

def dataframeManagementSum(df_positive,df_negative,yearNumber,List_information):
    
    df_positive.loc[df_positive["year"] == yearNumber, "value"] = List_information[0]
    df_negative.loc[df_negative["year"] == yearNumber, "value"] = List_information[1]
    
    
    print(df_positive)
    
def dataframeManagement(df_positive_adjectives,df_negative_adjectives,df_positive_nouns,df_negative_nouns,yearNumber,List_information):
    
    df_positive_adjectives.loc[df_positive_adjectives["year"] == yearNumber, "value"] = List_information[0]
    df_negative_adjectives.loc[df_negative_adjectives["year"] == yearNumber, "value"] = List_information[1]
    df_positive_nouns.loc[df_positive_nouns["year"] == yearNumber, "value"] = List_information[2]
    df_negative_nouns.loc[df_negative_nouns["year"] == yearNumber, "value"] = List_information[3]
    

def dataframeManagementValue(df_pos_year_value,df_pos_year_valueC,df_yearNumber,List_information):
    
    df_pos_year_value.loc[df_pos_year_value["Type"]=="ValuePosAdj","value"]=List_information[0]
    df_pos_year_value.loc[df_pos_year_value["Type"]=="ValueNegAdj","value"]=List_information[1]
    df_pos_year_value.loc[df_pos_year_value["Type"]=="ValuePosNouns","value"]=List_information[2]
    df_pos_year_value.loc[df_pos_year_value["Type"]=="ValueNegNouns","value"]=List_information[3]
    
    df_pos_year_valueC.loc[df_pos_year_valueC["Type"]=="ValuePosClusters","value"]=List_information[4]
    df_pos_year_valueC.loc[df_pos_year_valueC["Type"]=="ValueNegClusters","value"]=List_information[5]
    
    
def dataframeManagementClusters(df_positive_clusters,df_negative_clusters,yearNumber,resultPositive,resultNegative):
    
    df_positive_clusters.loc[df_positive_clusters["year"] == yearNumber, "value"] = resultPositive
    df_negative_clusters.loc[df_negative_clusters["year"] == yearNumber, "value"] = resultNegative  

def dataframeManagementClusters2(df_pos_year_valueC,yearNumber,resultPositive,resultNegative):
    
    df_pos_year_valueC.loc[df_pos_year_valueC["Type"]=="ValuePosClusters","value"]=resultPositive
    df_pos_year_valueC.loc[df_pos_year_valueC["Type"]=="ValueNegClusters","value"]=resultNegative
    
    
def dataframeManagementValue2(df_pos_year_value,yearNumber,List_information):
    
    df_pos_year_value.loc[df_pos_year_value["year"]== yearNumber,"value"]=List_information
    df_pos_year_value.loc[df_pos_year_value["year"]== yearNumber,"value"]=List_information
    df_pos_year_value.loc[df_pos_year_value["year"]== yearNumber,"value"]=List_information
    df_pos_year_value.loc[df_pos_year_value["year"]== yearNumber,"value"]=List_information  