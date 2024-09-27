### **Assignment 1 - k-Nearest Neighbors (k-NN)**

#### Overview
This assignment covers the implementation and evaluation of the **k-nearest neighbors (k-NN)** algorithm, focusing on risk calculation, data visualization, noise impact, and the effect of higher dimensions on model performance.

#### Key Tasks

- **Risk Calculation**: Calculated 0-1 loss risk for Bayes-optimal and constant classifiers based on provided distributions.
- **Data Visualization**: Generated scatter plots for binary-labeled datasets and analyzed class separability and the effect of outliers.
- **Model Training and Evaluation**: Implemented a k-NN classifier, optimized k-values, and visualized error rates across different values.
- **Noise Impact**: Assessed the impact of added noise on the classifier’s performance by comparing original vs. noisy datasets.
- **Dimensionality Impact**: Evaluated k-NN performance with added random features and analyzed how increasing dimensions affected error rates.
- **Error Analysis**: Compared k-NN’s performance with theoretical models and explored how overfitting was influenced by noise and dimensionality.

---

### **Assignment 2 - Gaussian Classifier & Bias-Variance Decomposition**

#### Overview
This assignment explores the implementation of a **Gaussian classifier** and the **bias-variance tradeoff**, focusing on model evaluation and generalization.

#### Key Tasks

- **Gaussian Classifier**: Implemented a Gaussian classifier to predict class labels based on normal distributions.
- **Bias-Variance Decomposition**: Analyzed bias and variance using model predictions to understand their effect on generalization error.
- **Risk & Error Analysis**: Computed 0-1 loss and mean squared error for Gaussian models, exploring the impact of bias-variance tradeoffs on classification accuracy.
- **Model Evaluation**: Evaluated the classifier using accuracy, confusion matrices, and risk, comparing it with the Bayes-optimal classifier.
- **Visualization**: Generated visualizations of classifier boundaries and decision regions to assess model behavior.

---

### **Assignment 3 - Constrained Optimization & Support Vector Machines (SVMs)**

#### Overview
This assignment delves into **constrained optimization** techniques and the application of **Support Vector Machines (SVMs)** for binary classification tasks.

#### Key Tasks

- **SVM Implementation**: Applied SVMs with linear and non-linear kernels to classify binary datasets.
- **Optimization Techniques**: Explored **Karush-Kuhn-Tucker (KKT) conditions** and used them to understand the constraints in SVM optimization.
- **Dual Form SVM**: Implemented the dual form of SVM to solve constrained optimization problems with non-linear kernels.
- **Model Evaluation**: Visualized decision boundaries, support vectors, and margins to assess classification accuracy and model performance.
- **Kernel Exploration**: Experimented with different kernels (e.g., RBF, polynomial) to evaluate the impact of kernel choice on classification accuracy and computational complexity.

---

### **Assignment 4 - Decision Trees**

#### Overview
This assignment focuses on the development and analysis of **decision trees** for classification tasks, emphasizing splitting criteria and model performance.

#### Key Tasks

- **Tree Construction**: Built decision trees from scratch using **Gini impurity** and **information gain** for node splitting.
- **Tree Pruning**: Applied pruning techniques to prevent overfitting and improve generalization.
- **Hyperparameter Tuning**: Experimented with tree depth, minimum samples per split, and other parameters to improve model performance.
- **Model Evaluation**: Assessed the decision tree’s accuracy on test data, visualized its structure, and explored feature importance.
- **Error Analysis**: Analyzed how pruning reduced model complexity and overfitting while maintaining classification accuracy.

---

### **Assignment 5 - Ensemble Methods**

#### Overview
This assignment investigates various **ensemble learning techniques**, particularly focusing on **boosting** to enhance model performance.

#### Key Tasks

- **Boosting Implementation**: Developed an **AdaBoost** model to combine weak learners and improve overall classification accuracy.
- **Weak Learner Design**: Designed and trained weak learners (e.g., decision stumps) for boosting, focusing on minimizing individual errors.
- **Model Evaluation**: Analyzed the impact of boosting on reducing overfitting and improving accuracy across different datasets.
- **Learning Curves**: Visualized learning curves and evaluated performance improvements through cross-validation.
- **Error Analysis**: Explored the effect of increasing the number of weak learners on model performance and overfitting.

---

### **Assignment 6 - Logistic Regression**

#### Overview
This assignment covers the implementation of **logistic regression** for binary classification tasks, focusing on model fitting, optimization, and evaluation.

#### Key Tasks

- **Model Implementation**: Implemented logistic regression from scratch, calculating **cross-entropy loss** and using gradient descent for optimization.
- **Binary Classification**: Applied logistic regression to the **FashionMNIST** dataset, splitting data into training and test sets for validation.
- **Model Evaluation**: Visualized **ROC curves** and computed **AUC** to evaluate classification performance.
- **Hyperparameter Optimization**: Tuned logistic regression hyperparameters (e.g., learning rate, regularization) to improve accuracy.
- **Regularization Techniques**: Explored **L2 regularization** to reduce overfitting and improve model generalization.

---

### **Assignment 7 - Neural Networks & PyTorch**

#### Overview
This assignment introduces **neural networks** using **PyTorch**, with a focus on solving non-linear classification tasks and exploring the benefits of deeper networks.

#### Key Tasks

- **Model Construction**: Built a fully connected neural network with multiple layers, trained using **stochastic gradient descent** for binary classification.
- **XOR Problem**: Addressed the **XOR problem** to demonstrate the necessity of multi-layer networks for solving non-linearly separable tasks.
- **Activation Functions**: Experimented with different activation functions (e.g., **ReLU**, **sigmoid**) and analyzed their impact on learning.
- **Model Evaluation**: Visualized loss and accuracy curves over multiple epochs, assessing the performance of the neural network.
- **Overfitting Control**: Applied **dropout** and other regularization techniques to reduce overfitting during training.
