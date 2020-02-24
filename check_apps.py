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

def dropbox_check():
    dropbox_link = 'https://en.wikipedia.org/wiki/Dropbox_(service)'
    dropbox_ver_xpath = '//table[@class="infobox vevent"]/tbody/tr/td//text()'
    dropbox_ver_list = scrape_app_version(dropbox_link, dropbox_ver_xpath)
    dropbox_ver = dropbox_ver_list[7].split(' ')[0]

    print("Dropbox: {}".format(dropbox_ver))

def equalizer_apo_check():
    equalizer_apo_link = 'https://sourceforge.net/projects/equalizerapo/files'
    equalizer_apo_ver_xpath = '//tr[@class="folder "]/th/a/span/text()'
    equalizer_apo_ver_list = scrape_app_version(equalizer_apo_link, equalizer_apo_ver_xpath)
    equalizer_apo_ver = equalizer_apo_ver_list[0]

    print("EqualizerAPO: {}".format(equalizer_apo_ver))

def firefox_check():
    firefox_link = 'https://en.wikipedia.org/wiki/Firefox'
    firefox_ver_xpath = '//table[@class="infobox vevent"]/tbody/tr/td//text()'
    firefox_ver_list = scrape_app_version(firefox_link, firefox_ver_xpath)
    firefox_ver = firefox_ver_list[21].split(' ')[0]

    print("Firefox: {}".format(firefox_ver))

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

def greenshot_check():
    greenshot_link = 'https://getgreenshot.org/downloads'
    greenshot_ver_xpath = '//div[2]/div[1]/div[1]/text()'
    greenshot_ver_list = scrape_app_version(greenshot_link, greenshot_ver_xpath)
    greenshot_ver = greenshot_ver_list[2].strip().split('-')[-1]

    print("Greenshot: {}".format(greenshot_ver))

def hashtab_check():
    hashtab_link = 'http://implbits.com/products/hashtab'
    hashtab_ver_xpath = '//a[@id="btn_download_now"]'
    hashtab_ver_list = scrape_app_version(hashtab_link, hashtab_ver_xpath)
    hashtab_ver = hashtab_ver_list[0].get("href").split('_')[1][1:]

    print("Hashtab: {}".format(hashtab_ver))

def hwinfo_check():
    hwinfo_link = 'https://www.hwinfo.com/download'
    hwinfo_ver_xpath = '//sub/text()'
    hwinfo_ver_list = scrape_app_version(hwinfo_link, hwinfo_ver_xpath)
    hwinfo_ver = hwinfo_ver_list[0].split(' ')[-1]

    print("HWInfo: {}".format(hwinfo_ver))

def itunes_check():
    itunes_link = 'https://en.wikipedia.org/wiki/ITunes'
    itunes_ver_xpath = '//table[@class="infobox vevent"]/tbody/tr/td//text()'
    itunes_ver_list = scrape_app_version(itunes_link, itunes_ver_xpath)
    itunes_ver = itunes_ver_list[8].split(' ')[0].strip()

    print("iTunes: {}".format(itunes_ver))

def klitecodec_check():
    klitecodec_link = 'https://codecguide.com/download_k-lite_codec_pack_standard.htm'
    klitecodec_ver_xpath = '//h4/text()'
    klitecodec_ver_list = scrape_app_version(klitecodec_link, klitecodec_ver_xpath)
    klitecodec_ver = klitecodec_ver_list[0].split(' ')[1]

    print("K-Lite Codec: {}".format(klitecodec_ver))

def mkvtoolnix_check():
    mkvtoolnix_link = 'https://www.fosshub.com/MKVToolNix.html'
    mkvtoolnix_ver_xpath = '//dd[@itemprop="softwareVersion"]/text()'
    mkvtoolnix_ver_list = scrape_app_version(mkvtoolnix_link, mkvtoolnix_ver_xpath)
    mkvtoolnix_ver = mkvtoolnix_ver_list[0]

    print("MKVToolnix: {}".format(mkvtoolnix_ver))

def obs_check():
    obs_link = 'https://obsproject.com/download'
    obs_ver_xpath = '//span[@class="dl_ver"]/text()'
    obs_ver_list = scrape_app_version(obs_link, obs_ver_xpath)
    obs_ver = obs_ver_list[0].split(' ')[-1]

    print("OBS: {}".format(obs_ver))

def open_shell_check():
    open_shell_link = 'https://github.com/Open-Shell/Open-Shell-Menu/releases'
    open_shell_ver_xpath = '//div[@class="f1 flex-auto min-width-0 text-normal"]/a/text()'
    open_shell_ver_list = scrape_app_version(open_shell_link, open_shell_ver_xpath)
    open_shell_ver = open_shell_ver_list[0]

    print("Open Shell: {}".format(open_shell_ver))

def python_check():
    python_link = 'https://www.python.org/downloads'
    python_ver_xpath = '//a[@class="button"]/text()'
    python_ver_list = scrape_app_version(python_link, python_ver_xpath)
    python_ver = python_ver_list[0].split(' ')[-1]

    print("Python: {}".format(python_ver))

def rufus_check():
    rufus_link = 'https://github.com/pbatard/rufus/releases/latest'
    rufus_ver_xpath = '//div[@class="f1 flex-auto min-width-0 text-normal"]/a/text()'
    rufus_ver_list = scrape_app_version(rufus_link, rufus_ver_xpath)
    rufus_ver = rufus_ver_list[0].split(' ')[1]

    print("Rufus: {}".format(rufus_ver))

def sublime_check():
    sublime_link = 'https://www.sublimetext.com/3dev'
    sublime_ver_xpath = '//p[@class="latest"]/text()'
    sublime_ver_list = scrape_app_version(sublime_link, sublime_ver_xpath)
    sublime_ver = sublime_ver_list[0].split(' ')[-1]

    print("Sublime Text: {}".format(sublime_ver))

def visual_studio_code_check():
    visual_studio_code_link = 'https://code.visualstudio.com/updates'
    visual_studio_code_ver_xpath = '//div[@class="col-sm-9 col-md-8 body"]/h1/text()'
    visual_studio_code_ver_list = scrape_app_version(visual_studio_code_link, visual_studio_code_ver_xpath)
    visual_studio_code_ver = visual_studio_code_ver_list[0].split(' ')[-1][0:-1]

    print("Visual Studio Code: {}".format(visual_studio_code_ver))

def winscp_check():
    winscp_link = 'https://winscp.net/eng/download.php'
    winscp_ver_xpath = '//a[@class="btn btn-primary btn-lg"]/text()'
    winscp_ver_list = scrape_app_version(winscp_link, winscp_ver_xpath)
    winscp_ver = winscp_ver_list[1].split(' ')[1]

    print("WinSCP: {}".format(winscp_ver))

def g_music_desktop_check():
    g_music_desktop_link = 'https://github.com/MarshallOfSound/Google-Play-Music-Desktop-Player-UNOFFICIAL-/releases'
    g_music_desktop_ver_xpath = '//div[@class="f1 flex-auto min-width-0 text-normal"]/a/text()'
    g_music_desktop_ver_list = scrape_app_version(g_music_desktop_link, g_music_desktop_ver_xpath)
    g_music_desktop_ver = g_music_desktop_ver_list[0].split(' ')[-1]

    print("Google Play Music Desktop: {}".format(g_music_desktop_ver))

def java_check():
    java_link = 'https://www.java.com/en/download/manual.jsp'
    java_ver_xpath = '//h4[@class="sub"]/text()'
    java_ver_list = scrape_app_version(java_link, java_ver_xpath)
    java_ver = ' '.join(java_ver_list[0].split(' ')[1:])

    print("Java: {}".format(java_ver))

def main():
    vc_check()
    seven_zip_check()
    audacity_check()
    calibre_check()
    cmder_check()
    crystaldiskinfo_check()
    crystaldiskmark_check()
    dropbox_check()
    equalizer_apo_check()
    peace_equalizer_check()
    search_everything_check()
    exiftool_check()
    faststone_check()
    ffmpeg_check()
    firefox_check()
    git_check()
    greenshot_check()
    hashtab_check()
    hwinfo_check()
    itunes_check()
    klitecodec_check()
    mkvtoolnix_check()
    obs_check()
    open_shell_check()
    sublime_check()
    visual_studio_code_check()
    winscp_check()
    python_check()
    rufus_check()
    g_music_desktop_check()
    java_check()

if __name__ == '__main__':
    main()
