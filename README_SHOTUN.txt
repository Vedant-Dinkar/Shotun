Shotun Web Application was partially completed. The version with Flask Module couldn't be completed.
It contains some logic regarding the back-end programming.
The program has the logic that the data is stored on the Github Repository, inside the SHOTUNDATA.txt folder and according to the short-link entered by the user(Example: https://vedant-dinkar.github.io/Shotun/ZSfyNhOu, randomly generated using the Random module), the webpage of Shotun was supposed to read the incorrect URL(Since the sub-directory of ZSfyNhOu does not exist) and then redirect to the corresponding original long link, also by trying to use the requests library.
The short URL is randomly generated(To be redirected) and its corresponding data is written onto the SHOTUNDATA.txt file.

The Shotun Scraping Application uses the Selenium Module in order to scrape data from bit.ly.
First, the program sends the keys to bit.ly and then it takes out the link.
It has two versions:
1. CLI - Give a long link as input and get a short URL as output.
2. Tap(Tkinter) Application - It consists of a button that automatically reads your clipboard and also, automatically copies the shorter URL to your clipboard.
Try not to control the computer while the program is running.
