[![Codacy Badge](https://app.codacy.com/project/badge/Grade/cbe9dad067f94b799d4b5d79ab913a4e)](https://www.codacy.com/gh/colav/Inti?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=colav/Inti&amp;utm_campaign=Badge_Grade)

# Inti
Capture system from non scrapping data sources

## Example running save MAG in MongoDB
`python3 run_mamagloader.py --mag_dir=/storage/colav/mag_sample/ --db=MA`

## Example running request SciELO and build a MongoDB
`python3 run_scieloloader.py --db=scielo`

### Running creating an instance

```from ScieloRequest import ScieloRequest```\
```sr=ScieloRequest(db="Scielo")```

ScieloRequest has three methods to get collections, journals and articles. The next run sequence is recommended for good results.

- ```get_collections()```: To get collections from SciELO and its info about number of documents, countries, and other data. 
    - **How to use:** only run the method in the created instance.\
    **Example:** ```sr.get_collections()```
- ```get_journals()```: To get whole the journals from Scielo, saving the journals' data.
    - **How to use:** only run the method in the created instance.\
    **Example:** ```sr.get_journals()```
- ```get_articles()```: To get whole the articles from Scielo, saving the article data.
    - **How to use:** only run the method in the created instance.\
    **Example:** ```sr.get_journals()```

When run first method, a Mongo database is built. After run is finished correctly, the Mongo database has three collections: collections, journals and stage (articles). 

### Using checkpoints methods

To get a checkpoint to recover the downloaded articles state, the class has three methods.

- ```create_cache()```: This method builds a collection to verifies full downloaded journals.
    - **How to use:** only run the method in the created instance.\
    **Example:** ```sr.create_cache()```

If articles downloading is broke up, ```get_articles()``` method has two inner methods to verifie the downloaded articles, delete articles if journal has uncompleted downloaded items (articles) and continue from the latest fully downloaded journal.

#### **Checkpoint methods used by ```get_articles()``` method**

Next three methods are used in by ```get_articles()``` in order to avoid repated documents in Mongo database.\
- ```update_cache(id_journal)```: This method updates download status key to one when a journal has been completelly downloaded.
- ```check_cache()```: Verifies which journals have been downloaded. If all journal articles have been downloaded, this method avoid includes this journal in downloadable journals.
- ```delete_articles(id_journal)```: Delete articles from an uncompleted downloaded journal. The articles are delete in stage collection.

In both latest methods, ```id_journal``` refers to he document id (ObjectId) in databse, assigned by Mongo when a journal is saved by ```get_journal()``` in journal collection.

### Other checkpoints methods

- ```fix_cache()```: Re-build cache collecion. If there are downloaded articles and cache collection
all journals appear as not-downloaded, this method updates the cache with the correct values.
    - **How to use:** only run the method in the created instance.\
    **Example:** ```sr.fix_cache()```





