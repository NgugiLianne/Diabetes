# Diabetes Prediction Project

## Overview
This project focuses on predicting the likelihood of diabetes in individuals based on various health-related features. Using a dataset that encapsulates health attributes from numerous individuals, we employ a Random Forest machine learning model to assess and predict diabetes presence. This README outlines the dataset details, project setup, usage instructions, and contribution guidelines.

## Dataset Introduction

The dataset employed in this project contains health-related information pertinent to diabetes diagnosis. Here are the attributes included in the dataset:

- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration 2 hours after an oral glucose tolerance test
- **Blood Pressure**: Diastolic blood pressure (mm Hg)
- **SkinThickness**: Triceps skin fold thickness (mm)
- **Insulin**: 2-hour serum insulin (mu U/ml)
- **BMI**: Body mass index (weight in kg/(height in m)^2)
- **DiabetesPedigreeFunction**: A score representing the likelihood of diabetes based on family history
- **Age**: Age of the individual (years)
- **Outcome**: Binary variable (0 or 1) indicating absence or presence of diabetes

## Project Setup

To set up and run this project on your local machine, follow these steps:

### Prerequisites
Ensure you have Python installed on your system. You can download Python [here](https://www.python.org/downloads/). Additionally, you will need the following packages:
- numpy
- pandas
- scikit-learn

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NgugiLianne/diabetes-prediction.git
   cd diabetes-prediction
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project

To run the model and start making predictions:

1. Launch your Python environment:
   ```bash
   python
   ```

2. Import the model and load your data:
   ```python
   from model import DiabetesPredictor
   predictor = DiabetesPredictor()
   predictor.load_data('path_to_your_data.csv')
   ```

3. Train the model:
   ```python
   predictor.train()
   ```

4. Make predictions:
   ```python
   results = predictor.predict()
   print(results)
   ```

## Contributing

Contributions to improve the project are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

Please make sure to update tests as appropriate and adhere to the existing coding style.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Contact

For any further questions or suggestions, feel free to reach out via [GitHub Issues](https://github.com/your-username/diabetes-prediction/issues) or pull requests.

Thank you for your interest in contributing to the Diabetes Prediction Project!
