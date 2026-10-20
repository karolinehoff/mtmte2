from __future__ import print_function
from collections import Counter
from IPython.display import FileLink
import pandas as pd
import numpy as np

def parse(filename, cols):
    # Returns a list of queries

    df = pd.read_csv(filename, sep=',', encoding='utf-8',
                     usecols=cols.keys(), dtype=cols, keep_default_na=False)
    
    query_col = next(col for col in cols if col != 'searches')

 #   query_col = 'search string cleaned'
    queries = []
    n = 0
    for idx, row in df.iterrows():
        n += 1
        for _ in range(row['searches']):
            queries.append(row[query_col])
    print('%s: Read %d rows' % (filename, n))
    return queries

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

# Zero result queries set stats, original search string
print('Zero Result searches, original search string stats')
qr = parse('zero-23-24.csv', {
        'searches': np.int32,
        'search string': str,
    })
            
print_stats(qr)
print()


# Zero result queries set stats, cleaned search string
print('Zero Result searches, search string cleaned stats')
qr = parse('zero-23-24.csv', {
        'searches': np.int32,
        'search string cleaned': str,
    })
            
print_stats(qr)
print()

#Lage tilfeldig uttrekk for analyse

def parse_and_sample(filename, cols, sample_size, random_seed):
    # Read the CSV file
    df = pd.read_csv(filename, sep=',', encoding='utf-8',
                     usecols=cols.keys(), dtype=cols, keep_default_na=False)
    
    # Randomly sample 50 rows from the filtered data
    sampled_df = df.sample(n=sample_size, random_state=random_seed)
    
    # Ensure the specified columns are included
    specified_columns = ['date', 'searches', 'search string', 'search string cleaned', 
                         'field searched', 'search type', 'active tab', 'resource type pre-filter', 
                         'signed in', 'on campus']
    
    # Filter the DataFrame to include only the specified columns
    sampled_df = sampled_df[specified_columns]
    
    # Export the sampled rows to a new CSV file
    sampled_df.to_csv('zero-23-24-sample.csv', index=False)
    
    # Print the results
    print(sampled_df)
    
    # Create download link
    from IPython.display import FileLink
    display(FileLink('zero-23-24-sample.csv'))

#Kjører uttrekk
cols = {'date': str, 'search string': str, 'search string cleaned': str, 
        'field searched': str, 'search type': str, 'active tab': str, 'resource type pre-filter': str, 
        'signed in': str, 'on campus': str, 'searches': int}

#Filnavn, kolonnene over, antall rader, nummer på random seed
parse_and_sample('zero-23-24.csv', cols, 50, random_seed=4)
