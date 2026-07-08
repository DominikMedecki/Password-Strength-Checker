# 🔐 Password Fortress

**Advanced Password Strength Analyzer & Secure Password Generator**

A modern, interactive web application built to help users create and evaluate strong passwords. Perfect demonstration of practical cybersecurity skills for job applications and portfolios.

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge)

## ✨ Features

- **Real-time Password Analysis** using `zxcvbn` (industry-standard strength estimator)
- **Crack Time Estimation** (offline & online scenarios)
- **Have I Been Pwned Integration** – safely checks if password was leaked
- **Strong Password Generator** with customizable options
- **Detailed Feedback & Suggestions** for improvement
- **Clean, Responsive UI** built with Streamlit

## 🚀 Live Demo

(You can deploy this for free on Streamlit Community Cloud)

## 📸 Screenshots

*(Add screenshots here after running the app)*

## 🛠️ Tech Stack

- **Python** 
- **Streamlit** – Web interface
- **zxcvbn** – Password strength estimation
- **Have I Been Pwned API** – Breach checking (k-anonymity)
- **Python Standard Library**

## 🏃‍♂️ Quick Start

### Prerequisites
- Python 3.8 or higher

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/password-strength-checker.git
cd password-strength-checker

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
# source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the app
streamlit run app.py
