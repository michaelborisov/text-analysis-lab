## Important comment
If do not want to download .ipynb files and face some issues with graph displaying, please refer to the [html](/html/) folder.

<br>

## Overview
Given set of financial reports, issued by companies, which are publicly traded. 
Apply machine learning techniques to find topics of paragraphs of documents.

- Use programming language`python3.4`;
- Use libraries `spacy`, `sklearn`;
- Apply methods `TF/IDF` and `LDA` to analyze given texts. 

<br>

## Folder/Structure
- [html](/html/) contains html-version of .ipynb files;
- [img](/img/) contains the charts from the result of two methods `TF/IDF` and `LDA`;
- [presentation](/presentation/) has the slides of our presentation;
- [src](/src/) has all the configurations we needed;
- file [LDA](/LDA.ipynb) apply the method `LDA`;
- file [TFIDF](/TFIDF_company_chart.ipynb) apply the method `TF/IDF`.

<br>

## Theory and Algorithm

### Preprocessing
- Remove all the unnecessary symbols;
- Remove all the stop words;
- Remove all the numbers;
- Classify all the words with their lemma.

### TF/IDF
- Stands for **term frequency-inverse document frequency**
- Our goals: 
    1. Find the most important words for certain text; 
    2. Learn the trend for this words during several years.
    3. Apply LSI technique at TF/IDF matrix to implement an information query program.

### LDA
- Stands for **Latent Dirichlet Allocation**
- Our goals: 
    1. Find several topics from certain text; 
    2. Find paragraphs in the text, which are mostly related to the topic; 
    3. Learn the trend for topics during several years.

<br>

## Reference
- library spacy: https://spacy.io/ 
- library sklearn: http://scikit-learn.org/stable/ 
- Wikipedia for TF-IDF: https://en.wikipedia.org/wiki/Tf%E2%80%93idf
- Wikipedia for LSI: https://en.wikipedia.org/wiki/Latent_semantic_analysis
- Blei, D.M., Ng, A.Y. and Jordan, M.I., 2003. Latent dirichlet allocation. Journal of machine Learning research, 3(Jan), pp.993-1022.

