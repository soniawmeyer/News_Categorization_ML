# News_Categorization_ML
A comparison of feature extraction methods and difference machine learning models on news classification.

With the growing digital world and text content being generated every millisecond, news comes in various contexts and to connect these articles to the right audience, they need to be classified. 
 
By using pre-labeled examples as training data, machine learning algorithms can learn the different associations between pieces of text, and that a particular output (i.e., category) is expected for a particular input (i.e., text). A “category” is the predetermined classification that any given text could fall into. While there exists research work on various approaches for text classification problems, in order to achieve this, we present a comprehensive approach to the text classification problem by using effective data preprocessing techniques, experiment different Natural Language Processing methods for feature extraction and different supervised learning algorithms - Naive Bayes, SVM, Logistic Regression & Random Forest, for classification. Our objective is to compare which feature extraction techniques and algorithms would aid in building an accurate classification model.


- Why is there a need for efficient pre-processing techniques? 

The first step towards training a machine learning NLP classifier is feature extraction: a method is used to transform each text into a numerical representation in the form of a vector.
 
Text classification problems usually tend to have high dimensional feature spaces, hence, mitigating the feature space without compromising on the accuracy of the classification becomes extremely important. This requires preprocessing techniques to convert the data into a structured format in order to extract effective features to aid in better classification.
 
We present a comprehensive approach to the text classification problem by using effective data preprocessing techniques, experiment different Natural Language Processing methods for feature extraction using - Bag of Words, TF-IDF & Word2Vec 

Bag of Words - is a feature extraction method which shows the vocabulary and the occurrence of the vocabulary in a document.

TF-IDF - TF-IDF reflects how important a certain word is to a document in a collection of documents.

Word2vec - Words are plotted in a multidimensional vector space, where similar words are closer to each other and the words surrounding a word provide the context to the word. The accuracy of the model is determined by the number of times the model sees the words within the same context throughout the dataset that is trained on. 

- Classification Models 

Then, the machine learning algorithm is fed with training data that consists of pairs of feature sets (vectors for each text example) and tags (e.g. sports, politics) to produce a classification model. 



