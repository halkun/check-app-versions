import lxml.html
import requests

def scrape_app_version(web_url, web_xpath):
    # Web Scrape from online
    my_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"}

    page = requests.get(web_url, headers=my_headers)
    tree = lxml.html.fromstring(page.content)

    app_version = str(tree.xpath(web_xpath)[0])

    return app_version

def main():
    zip_link = "https://www.7-zip.org/download.html"
    zip_ver_xpath = '//tr/td[2]/p[1]/b/text()'
    zip_ver = scrape_app_version(zip_link, zip_ver_xpath)
    print("7zip Online: {}".format(zip_ver))

    vc_link = 'https://github.com/abbodi1406/vcredist/releases'
    vc_ver_xpath = '//div[@class="f1 flex-auto min-width-0 text-normal"]/a/text()'
    vc_ver = scrape_app_version(vc_link, vc_ver_xpath)
    print("VC Redist Online: {}".format(vc_ver))

    audacity_link = 'https://www.fosshub.com/Audacity.html'
    audacity_xpath = '//dd[@itemprop="softwareVersion"]/text()'
    audacity_ver = scrape_app_version(audacity_link, audacity_xpath)
    print("Audacity Online: {}".format(audacity_ver))


if __name__ == '__main__':
    main()
