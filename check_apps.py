import lxml.html
import requests


def scrape_app_version(app_link, ver_xpath):
    my_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"}

    page = requests.get(app_link, headers=my_headers)
    tree = lxml.html.fromstring(page.content)
    app_version = tree.xpath(ver_xpath)

    return app_version

def seven_zip_check():
    zip_link = "https://www.7-zip.org/download.html"
    zip_ver_xpath = '//tr/td[2]/p[1]/b/text()'
    zip_ver_list = scrape_app_version(zip_link, zip_ver_xpath)
    zip_ver = zip_ver_list[0].split(' ')[2]

    print("7zip online: {}".format(zip_ver))

def vc_check():
    vc_link = 'https://github.com/abbodi1406/vcredist/releases'
    vc_ver_xpath = '//div[@class="f1 flex-auto min-width-0 text-normal"]/a/text()'
    vc_ver_list = scrape_app_version(vc_link, vc_ver_xpath)
    vc_ver = vc_ver_list[0][1:]

    print("VC Redist online: {}".format(vc_ver))

def audacity_check():
    audacity_link = 'https://www.fosshub.com/Audacity.html'
    audacity_xpath = '//dd[@itemprop="softwareVersion"]/text()'
    audacity_ver_list = scrape_app_version(audacity_link, audacity_xpath)
    audacity_ver = str(audacity_ver_list[0])

    print("Audacity online: {}".format(audacity_ver))

def calibre_check():
    calibre_link = 'https://calibre-ebook.com/download_windows'
    calibre_xpath = '//div[@id="download_block"]/div/text()'
    calibre_ver_list = scrape_app_version(calibre_link, calibre_xpath)
    calibre_ver = calibre_ver_list[1].split(' ')[1]

    print("Calibre online: {}".format(calibre_ver))

def cmder_check():
    cmder_link = 'https://github.com/cmderdev/cmder/releases'
    cmder_ver_xpath = '//div[@class="f1 flex-auto min-width-0 text-normal"]/a/text()'
    cmder_ver_list = scrape_app_version(cmder_link, cmder_ver_xpath)
    cmder_ver = cmder_ver_list[0][1:]

    print("cmder online: {}".format(cmder_ver))

def main():
    seven_zip_check()
    vc_check()
    audacity_check()
    calibre_check()
    cmder_check()

if __name__ == '__main__':
    main()
