#!/usr/bin/env python
# coding: utf-8

# # Financial Probabilities

# # #1
# ### At first glance, this csv file seems to be containing important financial data on thousands of individuals. The data is most likely used to detect certain individuals that may have financial issues/problems. For instance, you can see how many times each individual took 30+ or 90+ days past due on their bills, you can see their debt ratio, number of dependents, and so much more. This type of data would be extremely important in evaluating personal financial situations.

# # #2

# In[22]:


import pandas as pd
def loadAndCleanData(file):
    data = pd.read_csv(file)
    data.fillna(value = 0, inplace = True)
    return data


# # #3

# In[4]:


credit = loadAndCleanData("creditData.csv")


# # #4

# In[59]:


import matplotlib.pyplot as plt
def computePDF (columnName, dataSet):
    newPlot = dataSet[columnName].plot.kde()
    plt.show(newPlot)
    
header = list(credit.columns.values)
for x in header:
    computePDF(x, credit)


# # #5

# In[81]:


def viewDistribution(columnName, dataSet):
    newPlot = dataSet.hist(column = columnName)
    plt.show(newPlot)


# In[82]:


columns = list(credit.columns.values)
for x in columns:
    viewDistribution(x, credit)


# # #6

# In[79]:


def viewLogDistribution(columnName, dataSet):
    newPlot =dataSet.hist(column = columnName, log = True)
    plt.show(newPlot)


# In[80]:


logCol = list(credit.columns.values)
for x in logCol:
    viewLogDistribution(x, credit)


# # #7

# In[70]:


credit['ageBin'] = pd.qcut(credit['age'], q=3, duplicates = 'drop')
credit['DebtRBin'] = pd.qcut(credit['DebtRatio'], q=3, duplicates = 'drop')
credit['unsecuredLines'] = pd.qcut(credit['RevolvingUtilizationOfUnsecuredLines'], q=3, duplicates = 'drop')
credit['30days'] = pd.qcut(credit['NumberOfTime30-59DaysPastDueNotWorse'], q=3, duplicates = 'drop')
credit['monthlyInc'] = pd.qcut(credit['MonthlyIncome'], q=3, duplicates = 'drop')
credit['linesAndLoans'] = pd.qcut(credit['NumberOfOpenCreditLinesAndLoans'], q=3, duplicates = 'drop')
credit['90days'] = pd.qcut(credit['NumberOfTimes90DaysLate'], q=3, duplicates = 'drop')
credit['reLandL'] = pd.qcut(credit['NumberRealEstateLoansOrLines'], q=3, duplicates = 'drop')
credit['60days'] = pd.qcut(credit['NumberOfTime60-89DaysPastDueNotWorse'], q=3, duplicates = 'drop')
credit['numbDep'] = pd.qcut(credit['NumberOfDependents'], q=3, duplicates = 'drop')

credit.head()


# In[69]:


#bins for age column
credit['ageBin'].value_counts()


# In[44]:


#bins for DebtRatio column
credit['DebtRBin'].value_counts()


# In[45]:


#bins for RevolvingUtilizationOfUnsecuredLines column
credit['unsecuredLines'].value_counts()


# In[46]:


#bins for Monthly Income column
credit['monthlyInc'].value_counts()


# In[47]:


# bins for NumberOfOpenCreditLinesAndLoans column
credit['linesAndLoans'].value_counts()


# In[61]:


# bins for NumberOfTime30-59DaysPastDueNotWorse column
credit['30days'].value_counts()


# In[71]:


#bins for NumberOfTimes90DaysLate column
credit['90days'].value_counts()


# In[73]:


#bins for NumberRealEstateLoansOrLines column
credit['reLandL'].value_counts()


# In[74]:


#bins for NumberOfTime60-89DaysPastDueNotWorse column
credit['60days'].value_counts()


# In[78]:


#bins for NumberOfDependents column
credit['numbDep'].value_counts()


# # #8

# In[57]:


def computeDefaultRisk(column, feature, bin, Dataframe):
    count = 0.0
    count2 = 0.0
    for i,datapoint in Dataframe,itterows():
         if datapoint[feature] >= bin[0] and datapoint[feature] < bin[1]:
            count += 1
            if dataPoints[column]==1:
                count2+=1
    totalData = len(data)
    probability = count/totalData
    probability2 = count2/totalData
    print(probability2/probability)
    return probability2/probability


# # #9

# In[86]:


#view.computeDefaultRisk(column, feature, bin, Dataframe)
print(computeDefaultRisk("age", [0,40], credit))


# # Rating Schemes

# # #10

# In[83]:


newLoans = loadAndCleanData("newLoans.csv")


# # #11

# In[90]:


def predictDefaultRisk(row, df, weight):
    


# # #12

# In[ ]:





# # #13

# In[92]:


import matplotlib.pyplot as plt
def computePDF (columnName, dataSet):
    newPlot = dataSet[columnName].plot.kde()
    plt.show(newPlot)
    
loans = list(newLoans.columns.values)
for x in loans:
    computePDF(x, newLoans)


# In[ ]:




