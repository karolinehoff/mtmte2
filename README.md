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

## Notes

### The 2018 study 
* The data used in Huurdeman, H. C., Aamodt, M., & Heggø, D. M. (2018). “More than Meets the Eye” – Analyzing the Success of User Queries in Oria. Nordic Journal of Information Literacy in Higher Education, 10(1), 18–36. https://doi.org/10.15845/noril.v10i1.270 can be found at https://github.com/uio-library/virak_paper_data

### Data prep
* The `search sting cleaned` is a cleaned column based on `search string` added to both `popular-23-24.csv` and `zero-23-24.csv` in OpenRefine. The text was cleaned and normalized by removing special characters, trimming whitespace, and converting to lowercase, using the following GREL expression:

```javascript
value.replace(/[^a-zA-Z0-9\sÀ-ÖØ-öø-ÿ]/, "")
     .replace(/\s+/, " ")
     .toLowerCase()
     .trim()
```
### Note on Privacy

The risk that search queries can identify the user behind the queries indirectly should be taken seriously. The identification risk in this dataset is small because there are no anonymized user identifiers included. There are thus no links between different queries, and identifying a user from a single query is much harder than identifying one from a series of queries over time.

There is nothing that prevents a single query from being revealing, but we have yet to see examples of anything that resembles the kind of revealing searches you find in general purpose search engines like Google. Oria searches tend to be “business-like”, to-the-topic.

Finally, we have removed information that could potentially guide identification together with other information, such as the time of the day a search was made, or the browser or operating system used.
