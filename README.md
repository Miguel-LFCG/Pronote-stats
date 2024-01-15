# Pronote Stats 📚🔗

Pronote stats is a Python-based project designed to enhance the functionality of Pronote, a web-based school management system. This project includes features such as Baccalauréat (Bac) exam data generation, Pronote API integration, and more.

## Table of Contents 🗂

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation 🚀

To get started with LFCG Pronote, follow these steps:

```bash
git clone https://github.com/your-username/LFCG-Pronote.git
cd LFCG-Pronote
pip install -r requirements.txt
```

# Usage 🖥️

The project consists of the following files:

- `data_bac_gen.py`: Python script for generating Baccalauréat (Bac) exam data. **Progress : 10%**
- `data_sorted.py`: Python script for sorting data. **Progress : 90%**
- `main.py`: Main script for the LFCG Pronote project. **Progress : 80%** 
- `pronote.py`: Pronote API integration script. **Progress : 99%** _Extract other data for the Profil and  Pronostic section_
- `test_app.py`: Test script for the application. **Progress : 90%** _Average Not Calculated for a Test Profil_
- `static/`: Directory containing static files. **Progress : 95%** _Need to update the CSS for the Pronostic section_
- `templates/`: Directory containing templates. **Progress : 95%** _Implement other data in the Profil and  Pronostic_

## Configuration 🔧

To use LFCG Pronote for your college/lycée, you need to update the Pronote school web address in the `pronote.py` script. Open `pronote.py` and locate the following line:

```python
client = pronotepy.Client(
    'https://demo.index-education.net/pronote/eleve.html',  # Replace this line
      ...
```
Replace the URL in the parentheses with the web address of your Pronote school. This ensures that the application interacts with the correct Pronote instance.

## Example Usage 📄

1. Run the main application:

```bash
   python main.py
```

2. Access the application in your web browser by navigating to http://localhost:5000.

## Contributing 🤝

Contributions to LFCG Pronote are welcome! If you find any issues or have ideas for improvement, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as per the terms of the license.
