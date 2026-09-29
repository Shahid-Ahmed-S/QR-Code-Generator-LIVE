# QR Code Generator

A simple web-based QR Code Generator built with Python and Flask. The application allows users to enter text or a URL and generate a QR code instantly.

## Features

* Generate QR codes from text or URLs
* Simple and user-friendly interface
* Instant QR code generation
* Web-based application
* QR code image generation

## Technologies Used

* **Python**
* **Flask**
* **HTML**
* **CSS**
* **JavaScript**
* **qrcode**
* **Git & GitHub**

## Project Structure

```text
QR-Code-Generator/
├── static/
├── templates/
├── app.py
├── requirements.txt
└── README.md
```

## How It Works

1. Enter text or a URL into the input field.
2. Submit the form.
3. The Flask application processes the input.
4. A QR code is generated from the provided data.
5. The generated QR code is displayed to the user.

## Installation

Clone the repository:

```bash
git clone https://github.com/Shahid-Ahmed-S/QR-Code-Generator-LIVE.git
cd QR-Code-Generator-LIVE
```

Create a virtual environment:

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Flask application:

```bash
python app.py
```

Open the local URL displayed in the terminal, usually:

```text
http://127.0.0.1:5000
```

## Example

You can generate a QR code by entering:

```text
https://github.com/Shahid-Ahmed-S
```

The application generates a QR code containing the provided URL.

## Future Improvements

* Add QR code download functionality
* Add customizable QR code colors
* Add logo support
* Add QR code history
* Improve the user interface

## Author

**Shahid Ahmed**

[GitHub](https://github.com/Shahid-Ahmed-S) | [LinkedIn](https://www.linkedin.com/in/shahidahmed08/)
