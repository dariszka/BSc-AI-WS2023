# U1 - Tabular Data, Dimensionality Reduction, and Clustering

### Overview
This assignment involves working with the **Breast Cancer Wisconsin dataset**, focusing on tabular data analysis, dimensionality reduction, and clustering techniques.

### Key Tasks

- **Data Exploration**  
  - Analyzed a dataset with 30 features and 569 samples.
  - Classified data into two classes: malignant vs. benign.

- **Dimensionality Reduction**
  - **PCA**: Reduced 30-dimensional data to 2 dimensions for class visualization.
  - **t-SNE**: Further dimensionality reduction using t-SNE, optimized for better class separation.

- **Clustering**
  - Applied **k-Means Clustering** with different values of k (2 and 3).
  - Implemented **Affinity Propagation** to discover clusters and analyze data patterns.

--------------

# U2 - Reading, Handling and Visualization of Datasets

### Overview
This assignment involves tasks related to image manipulation, color segmentation, and audio signal processing.

### Key Tasks

- **Image Processing**
  - Loaded and visualized an image of a river, then performed cropping and channel analysis.

- **Color Segmentation**
  - Experimented with color thresholds to segment the river from its background.

- **Audio Signal Processing**
  - Generated and combined sine waves to create complex audio, then used Fourier transforms to analyze and decompose the signal.

--------------

# U3 - Supervised Machine Learning Basics

### Overview
This assignment introduces fundamental **supervised learning techniques**, including polynomial regression and k-Nearest Neighbors (k-NN), and involves tasks related to model evaluation and feature selection using the Breast Cancer Wisconsin dataset. 

### Key Tasks

- **Polynomial Regression**  
  - Fitted polynomial models of varying degrees to noisy data to determine the best fit without overfitting.

- **Data Preparation and Exploration**  
  - Loaded and examined the Breast Cancer dataset, isolating relevant features and labels for classification tasks.

- **Model Training and Evaluation**  
  - Split the dataset into training and test sets.
  - Evaluated k-NN classifiers with various k-values to identify the optimal parameter for classification accuracy.

- **Feature Selection and Model Optimization**  
  - Experimented with different feature subsets and combinations to enhance model performance.
  - Implemented Random Forest classifiers to explore feature combinations and estimator settings for improved accuracy.

- **Advanced Feature Combinations**  
  - Automated the process of finding the best feature combinations and model configurations using combinations and grid search techniques.

--------------


# U4 - Logistic Regression as a Door Opener to Deep Learning

### Overview
This assignment explores **logistic regression**, focusing on synthetic data generation, model fitting, and hyperparameter optimization using the FashionMNIST dataset.

### Key Tasks

- **Data Creation and Visualization**  
  - Generated synthetic datasets and visualized the data with linear models.
  - Applied optimization techniques to fit models and minimize Mean Squared Error (MSE).

- **Binary Classification**
  - Developed and optimized a logistic regression model for binary classification.
  - Evaluated model performance and visualized results using cross-entropy loss.

- **FashionMNIST Dataset**
  - Processed and split the FashionMNIST dataset.
  - Optimized logistic regression hyperparameters to achieve high accuracy and analyzed test set performance.

- **PyTorch Implementation**
  - Implemented key functions using PyTorch, including tensor operations and automatic differentiation for gradient computation.

--------------

# U5 - Your First Neural Networks

### Overview
This assignment covers the creation, optimization, and evaluation of neural network models using both synthetic datasets and the FashionMNIST dataset. It provides a hands-on introduction to basic neural network concepts, logistic regression, and practical PyTorch implementation.

### Key Tasks

- **Synthetic Data Modeling**
  - Created polynomial and logistic regression datasets.
  - Implemented models for polynomial fitting and binary classification.
  - Evaluated and visualized model performance with loss functions and gradient descent.

- **Logistic Regression with PyTorch**
  - Developed logistic regression models with one and two input features.
  - Implemented models using PyTorch for binary classification tasks.
  - Optimized models with Gradient Descent and visualized loss landscapes.

- **Neural Network Implementation**
  - Built and trained a neural network with one hidden layer for the FashionMNIST dataset.
  - Conducted hyperparameter tuning and evaluated model performance using accuracy metrics.

- **Advanced Model Training**
  - Applied a more complex model with additional hidden layers to improve classification accuracy on a 2D dataset.
  - Compared performance between simpler and more complex models to determine effective feature separation.

- **PyTorch Utilization**
  - Utilized PyTorch for various tasks including model training, loss calculation, and optimization.
  - Applied standard techniques for reproducibility and performance evaluation.

--------------

# U6 - Convolutional Neural Networks

### Overview
This assignment concentrates on **image processing and convolutional neural networks (CNNs)**, with a focus on applying various image filters, comparing max pooling and strided convolution, and training a CNN on the SVHN dataset.

### Key Tasks

- **Image Filtering**
  - Implemented and applied Prewitt and Scharr operators to grayscale images to highlight edges.
  - Defined custom filters and tested their effects on images.

- **Convolutional Neural Networks**
  - Built and trained a CNN model using the SVHN dataset with custom layers and hyperparameters.
  - Analyzed the impact of different pooling sizes and strides on image features.

- **Model Evaluation**
  - Evaluated model performance using accuracy metrics and visualized training and validation losses.
  - Compared outputs from max pooling and strided convolution layers to understand their effects on feature extraction.

--------------

# U7 - Tricks of the Trade

### Overview
This assignment shows 'Tricks of the Trade' in **Convolutional Neural Networks (CNNs)**, emphasizing dataset handling, model creation, training, and evaluation using the provided `burgers_and_burritos` dataset.

### Key Tasks

- **Data Handling and Visualization**  
  - Downloaded and loaded images from the dataset.
  - Applied data augmentation and visualized a sample of images.

- **Model Creation and Visualization**
  - Created a pretrained CNN with 18 layers using `u7.create_cnn()`.
  - Visualized and compared the weights of the first layer before and after training.

- **Training and Evaluation**
  - Trained a custom CNN without batch normalization and residuals, then evaluated weight changes post-training.
  - Trained another CNN with batch normalization and residuals, analyzed weight changes and their impact.

- **PyTorch Implementation**
  - Implemented CNNs and training routines using PyTorch, including functions for gradient descent and error rate evaluation.

--------------