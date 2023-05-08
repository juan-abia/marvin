# Marvin
Personal assistant telegram bot. It's based on the fictional character [Marvin](https://hitchhikers.fandom.com/wiki/Marvin) from [The Hitchhiker's Guide to the Galaxy](https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy).

## Note
Even though he is super intelligent, Marvin doesn't have memory (for now), so it won't remember previous messages. My plan is to add a context window that resets every 24 hours.

## How to use
To start the bot follow the next steps:
1. Clone this repo and `cd` to it:
    ```
    git clone https://github.com/juan-abia/marvin.git
    cd marvin
    ```
2. Activate a virtual environment and install requirements:
    ```
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
3. Create a .env file and add your [openai api key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key) and your [telegram bot token](https://core.telegram.org/bots/features#botfather):
    ```
    MARVIN_TOKEN="<your_bot_token>"
    OPENAI_API_KEY="<your_openai_api_key>"
    ```
4. Run `main.py` and enjoy using your personal assistant!
    ```
    python main.py
    ```

### Run continuously (WIP)
To run the bot continuously, repeat the first 3 steps previously defined, then:

5. Run `install.py`. It will ask for you password so it can install the necessary files. 
    ```
    python install.py
    ```
    This script creates a service that is executed all the time. It's made for fedora (37), I think it could run without problems in other distros, but I'm not very familiar, so your might have to debug a bit. Unfortunately, the service doesn't use a virtual environment for now, so if want to use the service, you'll have to install the dependencies globally.
    
6. To check if the service is running: 
    ```
    sudo systemctl status marvin.service
    ```

## Contribution guide
Even though this is an experimental project, I'm open to contribution and feedback :)
