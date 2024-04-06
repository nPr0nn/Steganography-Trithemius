
#### <p align="center">Hide secret files inside a PNG of your choice without anyone noticing </p>

<p align="center">
  <img src="repo/logo.png" alt="Logo" width="30%"/>
</p>

<p align="center">
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License">
  </a>
</p>


# Steganography-Trithemius

Welcome to Trithemius.py, an Steganography tool to hide any type of file inside a PNG image of your choice! Its works by enconding the file bits inside the bit planes of the input image color channels. Encodes and Decodes blazingly fast by using code vectorization :D

## Example of Usage

| secret_message.txt | input_image.png | result_image.png |
|-----------|-----------| -----------|
| I am already far north of London, and as I walk in the streets of
Petersburgh, I feel a cold northern breeze play upon my cheeks, which
braces my nerves and fills me with delight. Do you understand this
feeling? This breeze, which has travelled from the regions towards
which...| ![img1](repo/monalisa.png) | ![img2](repo/encoded_monalisa.png) |


## Code Structure

    Trithemius /
    │
    ├── src/
    │   ├── banner.txt
    │   ├── my_bits.py
    │   ├── my_cv.py
    │   ├── my_cli.py
    │   ├── my_files_io.py
    │   ├── encode.py
    │   ├── decode.py
    │   └── inspect.py
    │
    ├── app.py
    └── unit_tests.py

## Features

- **Encoding**:   Hide files within PNG images using specified bit planes.
- **Decoding**:   Extract hidden files from encoded PNG images.
- **Inspecting**: Visualize bit planes of color channels for image analysis.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/trithemius.py.git
