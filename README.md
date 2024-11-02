# Text-to-Speech PDF Reader

This repository contains a Python script that converts the text from a PDF file into speech using the Google Text-to-Speech (gTTS) library and plays the audio file.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Explanation](#explanation)
- [Contributing](#contributing)


## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/text-to-speech.git
    cd text-to-speech
    ```

2. **Install Dependencies**:
    Ensure you have Python installed. Then, install the required libraries:
    ```sh
    pip install gtts PyPDF2
    ```

3. **Prepare Your PDF File**:
    Place your PDF file in the project directory. For this example, the PDF file is named `text1.pdf`.

## Usage

1. **Run the Script**:
    ```sh
    python text_to_speech.py
    ```

2. **Output**:
    - The script will convert the text from the PDF file to speech and save it as an audio file (`audio.wav`).
    - The audio file will be played automatically.

## Explanation

### Code Overview

The script includes the following key components:
- **Loading the PDF**: Uses `PdfReader` from PyPDF2 to load and read the PDF file.
- **Text Extraction**: Iterates over each page of the PDF to extract the text.
- **Text-to-Speech Conversion**: Uses `gTTS` to convert the extracted text to speech.
- **Audio Playback**: Saves the speech as an audio file and plays it using `os.system`.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add YourFeature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

