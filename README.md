# LMS-BOT-Selenium
* Automated Script for LMS activities. (only opening of links... discussion forum and assginments need to be done manually)


```terminal
git clone https://github.com/enigmavadali/LMS-BOT-Selenium
cd LMS-BOT-Selenium
pip install -r requirements.txt
```
* [Download selenium chrome web driver according to your system](https://chromedriver.storage.googleapis.com/index.html?path=2.38/)

Extract the driver and place it in the ..\selenium\webdriver\chrome folder in your selenium package.(Downloaded from requirements.txt)

#### Add the file path of the driver to your PATH variable in the environment variables of your system.
Skipping the above step will result in failed execution

* Run bot.py
```terminal
python bot.py
```

