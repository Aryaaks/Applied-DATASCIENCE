# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 16:06:49 2023

@author: Akshay
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Reading data from 'IRIS.csv'
iris = pd.read_csv(r"C:\Users\Akshay\Downloads\IRIS.csv")
print(iris.head(30))


def sepal_length():
    """
    This plots the sepal length of three species of iris flower
    """
    data = iris.groupby('species')[
        'sepal_length'].sum().to_frame().reset_index()
    # Creating the bar chart
    plt.bar(data['species'], data['sepal_length'],
            color=['yellow', 'green', 'red'])
    # Adding the aesthetics
    plt.title('BAR GRAPH')
    plt.xlabel('Species')
    plt.ylabel('sepal_length')
    # Show the plot
    plt.show()
    return


def species_percentage():
    """
    This plots the percentage of three species of iris flower
    """
    pi = iris['species'].value_counts()
    # plt.pie(pi)
    color = ("yellow", "green", "pink")
    plt.figure(figsize=(8, 10))
    #pi.plot(kind='pie',startangle=45,colors = color,explode=[0.1,0.1,0.1],shadow=True,autopct='%2.1f%%')
    pi.plot(kind='pie', startangle=45, colors=color,
            shadow=True, autopct='%2.1f%%')
    plt.legend(title="SPECIES", loc='upper right')
    return


# Reading data from 'tax.csv'
tax = pd.read_csv(r"C:\Users\Akshay\Downloads\tax.csv")
print(tax)


def expenditure():
    """
    This plots the percentage of expenditure of five conuntries from 1995 through 2020
    """
    switzerand_tax = tax.loc[(tax['Country Name'] == 'Switzerland') & (tax['Indicator Name'] ==
                                                                       'International tourism, expenditures (% of total imports)')].iloc[:, 4:].values.tolist()[0]

    canada_tax = tax.loc[(tax['Country Name'] == 'Canada') & (tax['Indicator Name'] ==
                                                              'International tourism, expenditures (% of total imports)')].iloc[:, 4:].values.tolist()[0]

    brazil_tax = tax.loc[(tax['Country Name'] == 'Brazil') & (tax['Indicator Name'] ==
                                                              'International tourism, expenditures (% of total imports)')].iloc[:, 4:].values.tolist()[0]

    italy_tax = tax.loc[(tax['Country Name'] == 'Italy') & (tax['Indicator Name'] ==
                                                            'International tourism, expenditures (% of total imports)')].iloc[:, 4:].values.tolist()[0]

    years = (tax.columns.values[4:]).astype(np.int16)

    plt.figure()
    plt.plot(years, switzerand_tax)
    plt.plot(years, canada_tax)
    plt.plot(years, brazil_tax)
    plt.plot(years, italy_tax)
    plt.legend(['Switzerland', 'Canada', 'Brazil', 'Italy'], loc='upper right')
    plt.title('LINE GRAPH ')
    plt.xlabel('YEARS')
    plt.ylabel('expenditures (% of total imports)')
    plt.yticks(np.arange(0, 11, 1))
    plt.xticks(np.arange(years.min(), years.max() + 1, 1), rotation=70)
    # Show the plot
    plt.show()
    return

# Calling function to visualise bar graph
sepal_length()
 # Calling function to visualise pie chart
species_percentage()

 # Calling function to visualise line graph
expenditure()
