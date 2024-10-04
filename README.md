Autonomous Vehicles Animal Detection
This project implements an animal detection system for autonomous vehicles using deep learning techniques.
Overview
The system uses a transfer learning approach with a pre-trained VGG16 model to classify images as either containing an animal or not. This binary classification is crucial for autonomous vehicles to detect potential hazards on the road.
Features

Data preprocessing and augmentation
Transfer learning using VGG16 model
Custom dense layers for final classification
Training with early stopping
Evaluation and result visualization

Requirements

TensorFlow
Keras
NumPy
PIL
Plotly
scikit-learn

Usage

Clone the repository:
Copygit clone https://github.com/Giovannicus/AnimalRec.git
cd AnimalRec

Run the Jupyter notebook or Python script to:

Load and preprocess the CIFAR-10 dataset
Set up data augmentation
Build and train the model
Evaluate and visualize results


Model Architecture
The model uses a pre-trained VGG16 as a base, with additional custom dense layers:

Flatten layer
Dense layers (1024, 256, 64, 16 units)
Dropout layer (0.2)
Final Dense layer with sigmoid activation for binary classification

Results
The training process includes:

20 epochs (with early stopping)
Adam optimizer
Binary crossentropy loss
Accuracy and precision metrics

Results are visualized using Plotly for easy interpretation.

eda_batch.py: Contains functions for exploratory data analysis
logo.py: Displays the project logo
result.py: Functions for plotting results

Saving and Loading
The trained model is saved as 'vgg16_mod.h5', and the training history is saved as 'training_history.json' for future reference and analysis.
Note
This project is designed to run in a Colab environment. If running locally, ensure all dependencies are installed and adjust file paths as necessary.