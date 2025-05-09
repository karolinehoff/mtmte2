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


# Popular queries set stats, whole set 
print('Whole dataset')
qr = parse('popular-23-24.csv', {
        'searches': np.int32,
        'search string cleaned': np.compat.unicode,
        'year': np.int32,
        'month': np.int32
    }, 2023, 1, 2024, 12)
print_stats(qr)
print()

# Popular queries set stats, the limited csv-file
print('Selected range')
qr = parse('popular-extracted-23-24.csv', {
        'searches': np.int32,
        'search string cleaned': np.compat.unicode,
        'year': np.int32,
        'month': np.int32
    }, 2023, 1, 2024, 12)
print_stats(qr)
print()


# In[5]:


# Find top 50 queries overall in the popular queries set
cols = {'year': int, 'month': int, 'search string cleaned': str, 'searches': int}
qr = parse('popular-23-24.csv', cols, 2023, 1, 2024, 12)

print()
qr_c = [[k, v] for k, v in Counter(qr).items()]
keys = [x[0] for x in qr_c]
counts = np.array([x[1] for x in qr_c], dtype=np.int32)
top50_idx = (np.argsort(counts)[-50:])[::-1]

for i, n in enumerate(top50_idx):
    print('%d. %s (%d)' % (i + 1, keys[n], counts[n]))
    
# Prepare data for export
export_data = []
for i, n in enumerate(top50_idx):
    export_data.append({'Rank': i + 1, 'Query': keys[n], 'Count': counts[n]})

# Convert to DataFrame
export_df = pd.DataFrame(export_data)

# Export to CSV
export_df.to_csv('top50_queries_overall.csv', index=False)

print()
print("Top 50 queries have been exported to 'top50_queries_overall.csv'.")

# Create download link
display(FileLink('top50_queries_overall.csv'))


# In[6]:


# Find top 50 queries within the limited csv-file

cols = {'year': int, 'month': int, 'search string cleaned': str, 'searches': int}
qr = parse('popular-extracted-23-24.csv', cols, 2023, 1, 2024, 12)

from collections import Counter
import numpy as np

# Assuming qr is the list of queries from the parse function
qr_c = [[k, v] for k, v in Counter(qr).items()]
keys = [x[0] for x in qr_c]
counts = np.array([x[1] for x in qr_c], dtype=np.int32)
top50_idx = (np.argsort(counts)[-50:])[::-1]

for i, n in enumerate(top50_idx):
    print('%d. %s (%d)' % (i + 1, keys[n], counts[n]))

    
# Prepare data for export
export_data = []
for i, n in enumerate(top50_idx):
    export_data.append({'Rank': i + 1, 'Query': keys[n], 'Count': counts[n]})

# Convert to DataFrame
export_df = pd.DataFrame(export_data)

# Export to CSV
export_df.to_csv('top50_queries_extracted.csv', index=False)

print()
print("Top 50 queries have been exported to 'top50_queries_extracted.csv'.")

# Create download link
display(FileLink('top50_queries_extracted.csv'))

