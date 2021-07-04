# Image-Classification-Cifar-10

Image Classification is a fundamental task that attempts to comprehend an entire image as a whole. 
The goal is to classify the image by assigning it to a specific label.

Image classification is a supervised learning problem: 
* define a set of target classes (objects to identify in images)
* And train a model to recognize them using labeled example photos.

In this project we are going to classify images from the Cifar-10 Dataset. In this project we're preprocessing the image and training/prediction the convolutional neural networks model.

This dataset consists of airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck as the objects.

In below image we can see a random image from each classes.
![classes](https://github.com/rohan300557/Image-Classification-Cifar-10/blob/main/src/classes_plot.png)

After training the model I have plotted the graph between accuracy and val_accuracy. 
In grapgh accuracy is the accuracy of a batch of training data and val_accuracy is the accuracy of a batch of testing data (data that have never been 'seen' by the model). So, it is common for validation accuracy to be lower than accuracy. 
![accuracy plot](https://github.com/rohan300557/Image-Classification-Cifar-10/blob/main/src/accuracy_graph.png)

The above curve shows the accuacry and validation accuracy during the training of our model. The accuracy becomes stable after some epochs (at approx 40-50 epochs).
### Image Classification Prediction Page:
For prdicting the image that the image belongs to which class we will use Streamlit framework.
We will save the model which we trained using Tensorflow.

    model.save('model/model.h5')

After saving the model let's run Streamlit. To run the Streamlit web page we will using following command:

    Streamlit run main.py
Now on web app we will input the image, as shown below:
![input](https://github.com/rohan300557/Image-Classification-Cifar-10/blob/main/src/web_page_1.png)
Now as we gave image as input we recived the output of Airplane as shown in below image. We gave Airplane image as input and we can give any type image as input to predict it. So, it seems are model has predicted well.
![output](https://github.com/rohan300557/Image-Classification-Cifar-10/blob/main/src/web_page_2.png)
