#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Cleaning Census Data


# In[6]:


import pandas as pd


# In[7]:


df = pd.read_csv("data/NST-EST2021-alldata.csv")


# In[8]:


class basic_clean:
    '''This is the class to clean data'''
    
    def __init__(self, data):
        '''The data should be a dataframe'''
        self.data = pd.read_csv(data)
    
    
    def rounding(self,data_frame,column_name):
        data_frame[column_name]=  round(data_frame[column_name],4)
        #data_frame
        print("The column " +column_name+ ": has been rounded")
        return data_frame[column_name]
  
    def slicing(self,data_frame):
        
        #df1 gives whole United States
        
        df1 =data_frame.query('REGION == "0" & DIVISION == "0" & STATE == 0')
        print("Dataframe df1 has been created containing summary of United States as whole")

        #df2 gives all regions
        df2 =data_frame.query('REGION != "0" & DIVISION == "0" & STATE == 0')
        print("Dataframe df2 has been created containing details of Regions")
        
        #df3 gives all states
        df3 =data_frame.query('REGION != "0" & DIVISION != "0"')
        print("Dataframe df2 has been created containing details of States")
        


# In[9]:



if __name__ == "__main__":
    initial = basic_clean("data/NST-EST2021-alldata.csv")
    
    initial.slicing(df)
    print(initial.rounding(df,'NPOPCHG_2020'))
    initial.rounding(df,'NPOPCHG_2021')


# In[ ]:




