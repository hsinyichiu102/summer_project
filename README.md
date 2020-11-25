# summer_project

We had an interview with three people in different age to collect their use experience of the chatbot on the market.    



We found that most of the business provided the flow-based chatbot for user to find out the answer of their questions and had a live person aside to connect with if there was any question that the chatbot cannot solve. Therefore, the project aims to provide a useful and efficient chatbot for business to provide the service with a virtual salesperson.
We are talking about the main types of the chatbot for business today and discussing the recommender systems of Content-based, Collaborative filtering and hybrid system. We used the three algorithms to build two models for the program: the TFIDF algorithm for searching the product and Doc2Vec and Word2Vec algorithm for predicting and recommending the product that users might prefer.
We found out that the data preprocessing for TFIDF algorithm is very important. 


If the program can receive the word much closer to the base of the form, then it increases the possibility to provide the item that matched what users need. In order to provide the item that matched the request, we used the Word2Vec model to search again the recommended product from Doc2Vec model. In this program, we used the Word2Vec and Doc2Vec at the same time. However, if we can use the Word2Vec algorithm when doing the data preprocessing, the efficiency of the program would be increased.
We implemented our programs into Facebook Messager. The platform that we believed it is a good opportunity for business to reach their main customer.

Keywords: intent-based chatbot, flowed-based chatbot, content-based recommender system, TFIDF algorithm, Word2Vec algorithm, Doc2Vec algorithm
