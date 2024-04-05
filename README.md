# UFC-MLP-ML-Model-Prediction
---
## The purpose of this project is to making prediction of UFC fight with utilize different Deep Learning and Machine learning models.


#### After the experience and model creation, the test accuracy of a Muti-Layer Perceptron model could reach a 66.12% of accuracy when making prediction after 70 Epoch of training


#### In terms of the Machine learning, I seeking the possibiliy of whether the log transformation of the data that already beeing preprocessed would gives a better accuracy, the result is no. The performance was compared between the log-transformed and non-transformed data on different model, at the end, the model is perform better with non-transformed data  than log-transformed data. Among the model, I would use the linear regression as the baseline model since it is not a best choice of using it in the classification task, I would use 0.5 as the threshold, it has 67.89% of accuracy when it is using non-transformed data. Among the model, he random forest have a slightly bump compared to the baseline with 68.84% when it is using non-transformed data, the Support Vector Machine with linear kernel also have a high score of 68.02% accuracy when using non-transformed data, the kernel of rbf is slightly worse with an accuracy of 66.67% on non-transformed data. The KNN is the worst among the model, it has an accuracy of 62.99% among all the model, which proves that it does not fit for this classification task since it does not beat the baseline model.
