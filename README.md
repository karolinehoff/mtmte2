This repository contains the data used in MTMTE2

## Contents

### Jupyter Notebooks
* `MTMTE2 POPULAR 23-24.ipynb`
  * Handles the **Popular Searches** dataset
  * Generates:
    * `popular-23-24-top-50.csv`
    * `mtmte1-popular-23-24-top-50.csv`
* `MTMTE2 ZERO 23-24.ipynb`
  * Handles the **Zero Result Searches** dataset
  * Generates:
    * `zero-23-24-sample.csv`


### CSV Files

* `popular-23-24.csv` is the complete "Popular Searches" dataset with 6367 rows, each containing aggregated data for a *month*
* `popular-23-24-top-50.csv` is the overall top 50 queries from the Popular Searches dataset

<br>

* `zero-23-24.csv` is the complete "Zero Results" dataset with 70149 rows, each containing aggregated data for a *day*
* `zero-23-24-sample.csv` is the sample of 50 random queries from the "Zero Results" dataset

<br>

* `popular-23-24-mtmte1.csv` is the "Popular Searches" dataset with 4847 rows, limited to match the date scope of the original study (Jan - Jun '23 + Nov '23 - Sep '24)
* `popular-23-24-top-50-mtmte1.csv` is the  top 50 queries from the *limited* Popular Searches dataset 
* `zero-23-24-mtmte1.csv` is the complete "Zero Results" dataset with 41042 rows, limited to match the date scope of the original study (Aug '23 - Sep '24)

## Notes

### Data prep
* The `search sting cleaned` is a cleaned column based on `search string` added to both `popular-23-24.csv` and `zero-23-24.csv` in OpenRefine. The text was cleaned and normalized by removing special characters, trimming whitespace, and converting to lowercase, using the following GREL expression:

```javascript
value.replace(/[^a-zA-Z0-9\sÀ-ÖØ-öø-ÿ]/, "")
     .replace(/\s+/, " ")
     .toLowerCase()
     .trim()
```
