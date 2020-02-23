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

    print("7zip: {}".format(zip_ver))

def vc_check():
    vc_link = 'https://github.com/abbodi1406/vcredist/releases'
    vc_ver_xpath = '//div[@class="f1 flex-auto min-width-0 text-normal"]/a/text()'
    vc_ver_list = scrape_app_version(vc_link, vc_ver_xpath)
    vc_ver = vc_ver_list[0][1:]

    print("VC Redist: {}".format(vc_ver))

def audacity_check():
    audacity_link = 'https://www.fosshub.com/Audacity.html'
    audacity_xpath = '//dd[@itemprop="softwareVersion"]/text()'
    audacity_ver_list = scrape_app_version(audacity_link, audacity_xpath)
    audacity_ver = str(audacity_ver_list[0])

    print("Audacity: {}".format(audacity_ver))

def calibre_check():
    calibre_link = 'https://calibre-ebook.com/download_windows'
    calibre_xpath = '//div[@id="download_block"]/div/text()'
    calibre_ver_list = scrape_app_version(calibre_link, calibre_xpath)
    calibre_ver = calibre_ver_list[1].split(' ')[1]

    print("Calibre: {}".format(calibre_ver))

def cmder_check():
    cmder_link = 'https://github.com/cmderdev/cmder/releases'
    cmder_ver_xpath = '//div[@class="f1 flex-auto min-width-0 text-normal"]/a/text()'
    cmder_ver_list = scrape_app_version(cmder_link, cmder_ver_xpath)
    cmder_ver = cmder_ver_list[0][1:]

    print("cmder: {}".format(cmder_ver))

def crystaldiskinfo_check():
    crystaldiskinfo_link = 'https://crystalmark.info/en/download'
    crystaldiskinfo_ver_xpath = '//div[@class="entry entry-content"]/h2[2]/text()'
    crystaldiskinfo_ver_list = scrape_app_version(crystaldiskinfo_link, crystaldiskinfo_ver_xpath)
    crystaldiskinfo_ver = crystaldiskinfo_ver_list[0].split(' ')[2]

    print("CrystalDiskInfo: {}".format(crystaldiskinfo_ver))

def crystaldiskmark_check():
    crystaldiskinfo_link = 'https://crystalmark.info/en/download'
    crystaldiskinfo_ver_xpath = '//div[@class="entry entry-content"]/h2[3]/text()'
    crystaldiskinfo_ver_list = scrape_app_version(crystaldiskinfo_link, crystaldiskinfo_ver_xpath)
    crystaldiskinfo_ver = crystaldiskinfo_ver_list[0].split(' ')[3]

    print("CrystalDiskInfo: {}".format(crystaldiskinfo_ver))

def equalizer_apo_check():
    equalizer_apo_link = 'https://sourceforge.net/projects/equalizerapo/files'
    equalizer_apo_ver_xpath = '//tr[@class="folder "]/th/a/span/text()'
    equalizer_apo_ver_list = scrape_app_version(equalizer_apo_link, equalizer_apo_ver_xpath)
    equalizer_apo_ver = equalizer_apo_ver_list[0]

    print("EqualizerAPO: {}".format(equalizer_apo_ver))

def peace_equalizer_check():
    peace_equalizer_link = 'https://sourceforge.net/projects/peace-equalizer-apo-extension/files'
    peace_equalizer_ver_xpath = '//table[@id="files_list"]/tbody/tr[7]/td[1]/abbr/text()'
    peace_equalizer_ver_list = scrape_app_version(peace_equalizer_link, peace_equalizer_ver_xpath)
    peace_equalizer_ver = peace_equalizer_ver_list[0]

    print("Peace Equalizer: {}".format(peace_equalizer_ver))

def search_everything_check():
    search_everything_link = 'https://www.voidtools.com/downloads'
    search_everything_ver_xpath = '//h2[@id="dl"]/text()'
    search_everything_ver_list = scrape_app_version(search_everything_link, search_everything_ver_xpath)
    search_everything_ver = search_everything_ver_list[0].split(' ')[-1]

    print("Search Everything: {}".format(search_everything_ver))

def exiftool_check():
    exiftool_link = 'https://exiftool.org'
    exiftool_ver_xpath = '//a[contains(text(),"exiftool-")]/text()'
    exiftool_ver_list = scrape_app_version(exiftool_link, exiftool_ver_xpath)
    exiftool_ver = exiftool_ver_list[0].split(' ')[-1].split('-')[-1][0:-4]

    print("Exiftool: {}".format(exiftool_ver))

def faststone_check():
    faststone_link = 'https://www.faststone.org/FSIVDownload.htm'
    faststone_ver_xpath = '//font[contains(text(),"FastStone Image Viewer")]/text()'
    faststone_ver_list = scrape_app_version(faststone_link, faststone_ver_xpath)
    faststone_ver = faststone_ver_list[-1].split(' ')[-2][0:3]

    print("FastStone: {}".format(faststone_ver))

def ffmpeg_check():
    ffmpeg_link = 'https://ffmpeg.zeranoe.com/builds'
    ffmpeg_ver_xpath = '//label[@class="btn btn-secondary active"]/text()'
    ffmpeg_ver_list = scrape_app_version(ffmpeg_link, ffmpeg_ver_xpath)
    ffmpeg_ver = ffmpeg_ver_list[1].strip()

    print("FastStone: {}".format(ffmpeg_ver))

def git_check():
    git_link = 'https://git-scm.com/download/win'
    git_ver_xpath = '//p[1]/strong[1]/text()'
    git_ver_list = scrape_app_version(git_link, git_ver_xpath)
    git_ver = git_ver_list[0]

    print("Git: {}".format(git_ver))

def main():
    seven_zip_check()
    vc_check()
    audacity_check()
    calibre_check()
    cmder_check()
    crystaldiskinfo_check()
    crystaldiskmark_check()
    equalizer_apo_check()
    peace_equalizer_check()
    search_everything_check()
    exiftool_check()
    faststone_check()
    ffmpeg_check()
    git_check()

if __name__ == '__main__':
    main()
