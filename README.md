# Text-to-Speech PDF Reader

This repository contains a Python script that converts the text from a PDF file into speech using the Google Text-to-Speech (gTTS) library and plays the audio file.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Explanation](#explanation)
- [Contributing](#contributing)
- [License](#license)

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
```python
from gtts import gTTS
from PyPDF2 import PdfReader
import os

# Load the PDF file
f = open('text1.pdf', 'rb')
pdf = PdfReader(f)
text = ''

# Extract text from each page
for pages in pdf.pages:
    text += pages.extract_text()

# Specify the language for the TTS
language = 'en'

# Convert the extracted text to speech
audio = gTTS(text=text, lang=language, slow=False)
audio.save('audio.wav')

# Play the audio file
os.system('audio.wav')
