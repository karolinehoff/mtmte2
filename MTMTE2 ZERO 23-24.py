#!/usr/bin/env python
# coding: utf-8

# In[1]:


from __future__ import print_function
from collections import Counter
from IPython.display import FileLink
import pandas as pd
import numpy as np


# In[2]:


def parse(filename, cols, start_year, start_month, end_year, end_month):
    # Returns a list of queries

    df = pd.read_csv(filename, sep=',', encoding='utf-8',
                     usecols=cols.keys(), dtype=cols, keep_default_na=False)
    
    # Convert year and month columns to integers
    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)
    
    # Filter the dataframe by the specified date range
    df = df[((df['year'] == start_year) & (df['month'] >= start_month)) |
            ((df['year'] > start_year) & (df['year'] < end_year)) |
            ((df['year'] == end_year) & (df['month'] <= end_month))]
    
    query_col = 'search string cleaned'
    queries = []
    n = 0
    for idx, row in df.iterrows():
        n += 1
        for _ in range(row['searches']):
            queries.append(row[query_col])
    print('%s: Read %d rows' % (filename, n))
    return queries


# In[3]:


def print_stats(qr):
    qd = set(qr)

    nchars_qr = np.array([len(x) for x in qr])
    nchars_qd = np.array([len(x) for x in qd])

    nwords_qr = np.array([len(x.split()) for x in qr])
    nwords_qd = np.array([len(x.split()) for x in qd])

    print('- Number of queries: %d' % len(qr))
    print('  - mean number of words: %.2f' % np.mean(nwords_qr))
    print('  - median number of words: %.2f' % np.median(nwords_qr))
    print('  - mean number of chars: %.2f' % np.mean(nchars_qr))
    print('  - median number of chars: %.2f' % np.median(nchars_qr))

    print('- number of distinct queries: %d' % len(qd))
    print('  - mean number of words: %.2f' % np.mean(nwords_qd))
    print('  - median number of words: %.2f' % np.median(nwords_qd))
    print('  - mean number of chars: %.2f' % np.mean(nchars_qd))
    print('  - median number of chars: %.2f' % np.median(nchars_qd))


# In[4]:


# Zero result queries set 2023 - 2024
print('Whole dataset')
qr = parse('zero-23-24.csv', {
        'searches': np.int32,
        'search string cleaned': np.compat.unicode,
        'year': np.int32,
        'month': np.int32
    }, 2023, 1, 2024, 12)
            
print_stats(qr)
print()


# Zero result queries set, Aug23-Sept24
print('Selected range')
qr = parse('zero-23-24.csv', {
        'searches': np.int32,
        'search string cleaned': np.compat.unicode,
        'year': np.int32,
        'month': np.int32
    }, 2023, 8, 2024, 9)
            
print_stats(qr)
print()

# Zero result queries set, Jan23-Feb24
print('Selected range')
qr = parse('zero-23-24.csv', {
        'searches': np.int32,
        'search string cleaned': np.compat.unicode,
        'year': np.int32,
        'month': np.int32
    }, 2023, 1, 2024, 2)
            
print_stats(qr)
print()


# In[5]:


#Lage tilfeldig uttrekk for analyse

def parse_and_sample(filename, cols, start_year, start_month, end_year, end_month, sample_size, random_seed):
    # Read the CSV file
    df = pd.read_csv(filename, sep=',', encoding='utf-8',
                     usecols=cols.keys(), dtype=cols, keep_default_na=False)
    
    # Convert year and month columns to integers
    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)
    
    # Filter the dataframe by the specified date range
    df = df[((df['year'] == start_year) & (df['month'] >= start_month)) |
            ((df['year'] > start_year) & (df['year'] < end_year)) |
            ((df['year'] == end_year) & (df['month'] <= end_month))]
    
    # Randomly sample 50 rows from the filtered data
    sampled_df = df.sample(n=sample_size, random_state=random_seed)
    
    # Ensure the specified columns are included
    specified_columns = ['date', 'searches', 'search string', 'search string cleaned', 
                         'field searched', 'search type', 'active tab', 'resource type pre-filter', 
                         'signed in', 'on campus']
    
    # Filter the DataFrame to include only the specified columns
    sampled_df = sampled_df[specified_columns]
    
    # Export the sampled rows to a new CSV file
    sampled_df.to_csv('sampled-zero-queries.csv', index=False)
    
    # Print the results
    print(sampled_df)
    
    # Create download link
    from IPython.display import FileLink
    display(FileLink('sampled-zero-queries.csv'))


# In[6]:


#Notat 07.05.2025: zero-complete.csv inneholder et par måneder fra 2025, og må derfor defineres 
#08.05.25: zero_23-24.csv er kun januar 2023 - desember 2024, og kan brukes

#Kjører uttrekk
cols = {'year': int, 'month': int, 'date': str, 'search string': str, 'search string cleaned': str, 
        'field searched': str, 'search type': str, 'active tab': str, 'resource type pre-filter': str, 
        'signed in': str, 'on campus': str, 'searches': int}

#Filnavn, kolonnene over, startår, startmåned, sluttår, sluttmåned, antall rader
parse_and_sample('zero-23-24.csv', cols, 2023, 1, 2024, 12, 50, random_seed=1)


