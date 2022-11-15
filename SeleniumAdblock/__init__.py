import os
from selenium import webdriver


class SeleniumAdblock:
    def __init__(self):
        """
        It creates a new instance of the ChromeOptions class.
        """
        self.options = webdriver.ChromeOptions()

    def _startAdBlock(self):
        """
        It adds the extension to the options object, which is then used to create the driver
        :return: The options for the browser.
        """
        self.options.add_extension(os.path.join(os.path.dirname(__file__), 'Ultimate-Ad-Blocker.crx'))
        self.options.add_extension(os.path.join(os.path.dirname(__file__), 'Popup-Blocker-strict.crx'))
        return self.options

    @staticmethod
    def _listaAdBlock():
        """
        It returns a list of all the files in the directory where the script is located, that end with the extension ".crx"
        :return: A list of all the files in the directory that end with .crx
        """
        lista = []
        for file in os.listdir(os.path.dirname(__file__)):
            if file.endswith(".crx"):
                lista.append(file.replace(".crx", ""))
        return lista

    def _startAdblockList(self, name):
        """
        It takes a string as an argument, checks if it's in a list of strings, and if it is, it adds the string to a list of
        strings

        :param name: The name of the extension you want to add
        :return: The options object is being returned.
        """
        if name not in self._listaAdBlock():
            raise ValueError("Extension not found")

        for file in self._listaAdBlock():
            if name in file.replace(".crx", ""):
                self.options.add_extension(os.path.join(os.path.dirname(__file__), file + ".crx"))

        return self.options

    def _startCustomAdBlock(self, path):
        """
        It takes a path to a Chrome extension, and adds it to the Chrome options

        :param path: The path to the extension file
        :return: The options object is being returned.
        """
        if not os.path.isfile(path):
            raise FileNotFoundError("File not found")

        self.options.add_extension(path)
        return self.options
