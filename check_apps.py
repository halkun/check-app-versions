from lxml import html
import requests

def scrape_app_version(web_url, web_xpath, ver_index):
    # Web Scrape from online
    my_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"}


    page = requests.get(web_url, headers=my_headers)
    tree = html.fromstring(page.content)

    # Download 7-Zip 19.00 (2019-02-21) for Windows
    str_raw = str(tree.xpath(web_xpath)[0])
    app_version = str_raw.split(' ')[ver_index]

    return app_version

def main():
    zip_link = "https://www.7-zip.org/download.html"
    zip_str_xpath = '//tr/td[2]/p[1]/b/text()'
    version_index = 2
    zip_ver = scrape_app_version(zip_link, zip_str_xpath, version_index)
    print("7zip Version online: {}".format(zip_ver))

if __name__ == '__main__':
    main()
