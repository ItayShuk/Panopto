import webbrowser
import panopto_api

chrome = "rC:\Program Files (x86)\Google\Chrome\Application\chrome.exe"


def main():
    browser = webbrowser.get(chrome)
    browser.open("rhttps://huji.cloud.panopto.eu/Panopto/Pages/Admin/RemoteRecorders/List.aspx#")


if __name__ == '__main__':
    main()
