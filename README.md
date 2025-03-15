
# Cougar AI Adorable Chatbot

This project features a Streamlit-based chatbot powered by Ollama's models. The chatbot is designed to interact with users in various tones, depending on the selected personality. It offers a flexible user interface to adjust the chatbot's creativity (temperature) and the tone of the responses. 

![Demo](/img/demo.png)

## Features
- **Interactive Chatbot**: Allows real-time communication with an AI assistant.
- **Personality Selection**: Choose from five different personalities: Friendly, Professional, Sarcastic, Encouraging, or Direct.
- **Temperature Adjustment**: Control the creativity of the responses by adjusting the temperature setting (range: 0.0 to 1.0).
- **Customizable Interface**: Built with Streamlit, allowing easy deployment and interaction.

## Requirements
To run this project, you'll need Python 3.x installed. The required dependencies are listed in the `requirements.txt` file.

### Installing Dependencies
To install all the dependencies, simply run the following command:

```bash
pip install -r requirements.txt
```

This will install:
- Streamlit
- langchain_ollama

### Install Ollama
To use the chatbot with Ollama's models, you need to install Ollama on your system. Ollama supports Windows, macOS, and Linux. Follow the installation instructions based on your operating system.

#### For Windows:
1. Download the [Ollama installer for Windows](https://ollama.com/download).
2. Run the installer and follow the setup instructions.

#### For macOS:
1. Download the [Ollama installer for macOS](https://ollama.com/download).
2. Open the `.dmg` file and follow the on-screen instructions to complete the installation.

#### For Linux:
1. For Debian-based distributions (Ubuntu, etc.), download and install the `.deb` package using:

    ```bash
    curl -fsSL https://ollama.com/download | sudo bash
    sudo apt install ollama
    ```

2. For RedHat-based distributions (Fedora, CentOS, etc.), use:

    ```bash
    curl -fsSL https://ollama.com/download | sudo bash
    sudo dnf install ollama
    ```

### Pulling the `gemma2:27b` Model
Before running the chatbot, you need to pull the `gemma2:27b` model. This can be done using the following command:

```bash
ollama pull gemma2:27b
```

This will download the model and prepare it for use in the chatbot.

## File Structure
- **chatbot.py**: Contains the logic for the chatbot, including the ability to set temperature, personality, and interaction.
- **main.py**: The Streamlit app that hosts the interface and allows user interaction with the chatbot.
- **misc/**: Folder containing assets like the logo for the chatbot interface.

## Running the Project
To run the project, simply execute the following command:

```bash
streamlit run main.py
```

This will launch the Streamlit app in your web browser, where you can interact with the chatbot.

## Customization
- **Change Model**: You can change the underlying model by updating the `model` parameter in the `Chatbot` class.
- **Adjust Settings**: The temperature and personality settings are adjustable via the sidebar in the Streamlit app.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
