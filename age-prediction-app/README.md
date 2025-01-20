# Age Prediction Application

This project is an age prediction application that utilizes OpenCV for face detection and DeepFace for age estimation. The application reads an image, detects faces, and predicts the age of the detected faces.

## Project Structure

```
age-prediction-app
├── src
│   ├── main.py        # Main logic for the age prediction application
├── requirements.txt   # List of dependencies
└── README.md          # Project documentation
```

## Requirements

To run this application, you need to install the following dependencies:

- OpenCV
- DeepFace

You can install the required packages using pip. Make sure to create a virtual environment for your project.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd age-prediction-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place your image in the project directory or specify the path in the `src/main.py` file.
2. Run the application:
   ```
   python src/main.py
   ```

The application will display the image with detected faces and their predicted ages.

## Additional Information

- Ensure that you have the necessary permissions to use the images for age prediction.
- The accuracy of age prediction may vary based on the quality of the input images and the model used by DeepFace.