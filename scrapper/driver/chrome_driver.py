import os
import subprocess as sp
from selenium import webdriver


class ChromeDriver:

    def __init__(self):
        path = sp.run("pwd", capture_output=True).stdout.decode().strip()+"/scrapper/driver/"
        print(f'{path=}')

        # download chrome driver https://chromedriver.storage.googleapis.com/index.html?path=84.0.4147.30/
        self.chromedriver_path = os.path.join(path, "chromedriver")
        print(f"{self.chromedriver_path=}")

        self.DEBUGGING = False

    def ___setup_web_driver___(self) -> webdriver:
        # setup Chrome Options:
        setup_options = webdriver.ChromeOptions()

        # on Debugging mode; the chrome window is visible, otherwise it's not visible.
        setup_options.headless = not self.DEBUGGING

        # link web-driver to chromedriver_path and include setup_options
        return webdriver.Chrome(self.chromedriver_path, options=setup_options)


if __name__ == "__main__":
    ChromeDriver().___setup_web_driver___()
