import lxml.html
import openpyxl
import os
import requests


# extract raw version data using the website's html xpath
def scrape_app_version(app_link, ver_xpath):
    my_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"}

    page = requests.get(app_link, headers=my_headers)
    tree = lxml.html.fromstring(page.content)
    app_version = tree.xpath(ver_xpath)

    return app_version

# import local copy with apps information
def load_apps_info():
    apps_wb = openpyxl.load_workbook('./apps_info.xlsx')
    apps_sheet = apps_wb['Sheet1']
    apps_data = {}

    max_row_plus = apps_sheet.max_row + 1

    for row in range(2, max_row_plus):
        app_var_cell = 'A' + str(row)
        app_name_cell = 'B' + str(row)
        app_local_ver_cell = 'C' + str(row)
        app_link_cell = 'D' + str(row)
        app_ver_xpath_cell = 'E' + str(row)

        temp_dict = {
            apps_sheet[app_var_cell].value: {
                apps_sheet['B1'].value: apps_sheet[app_name_cell].value,
                apps_sheet['C1'].value: apps_sheet[app_local_ver_cell].value,
                apps_sheet['D1'].value: apps_sheet[app_link_cell].value,
                apps_sheet['E1'].value: apps_sheet[app_ver_xpath_cell].value
            }
        }

        apps_data.update(temp_dict)

    # print(apps_data['visual_c']['app_name'])

    return apps_data

def get_app(download_link):
    os.system("start \"\" {}".format(download_link))
    input("wait...")

# check all apps to see for new updates
def check_apps_version():
    apps_dict = load_apps_info()
    # print(apps_dict)

    # specific syntax to capture the version string from different website
    for key in apps_dict:
        app_link = apps_dict[key]['app_link']
        app_ver_xpath = apps_dict[key]['app_ver_xpath']
        scrape_ver_list = scrape_app_version(app_link, app_ver_xpath)
        if key == 'visual_c':
            app_ver = scrape_ver_list[0][1:]
        elif key == 'seven_zip':
            app_ver = scrape_ver_list[0].split(' ')[2]
        elif key == 'audacity':
            app_ver = str(scrape_ver_list[0])
        elif key == 'calibre':
            app_ver = scrape_ver_list[1].split(' ')[1]
        elif key == 'cmder':
            app_ver = scrape_ver_list[0][1:]
        elif key == 'crystaldiskinfo':
            app_ver = scrape_ver_list[0].split(' ')[2]
        elif key == 'crystaldiskmark':
            app_ver = scrape_ver_list[0].split(' ')[3]
        elif key == 'dropbox':
            app_ver = scrape_ver_list[7].split(' ')[0]
        elif key == 'equalizer_apo':
            app_ver = scrape_ver_list[0]
        elif key == 'peace_equalizer':
            app_ver = scrape_ver_list[0]
        elif key == 'search_everything':
            app_ver = scrape_ver_list[0].split(' ')[-1]
        elif key == 'exiftool':
            app_ver = scrape_ver_list[0].split(' ')[-1].split('-')[-1][0:-4]
        elif key == 'faststone':
            app_ver = scrape_ver_list[-1].split(' ')[-2][0:3]
        elif key == 'ffmpeg':
            app_ver = scrape_ver_list[1].strip()
        elif key == 'firefox':
            app_ver = scrape_ver_list[21].split(' ')[0]
        elif key == 'git':
            app_ver = scrape_ver_list[0]
        elif key == 'greenshot':
            app_ver = scrape_ver_list[2].strip().split('-')[-1]
        elif key == 'hashtab':
            app_ver = scrape_ver_list[0].get("href").split('_')[1][1:]
        elif key == 'hwinfo':
            app_ver = scrape_ver_list[0].split(' ')[-1]
        elif key == 'itunes':
            app_ver = scrape_ver_list[8].split(' ')[0].strip()
        elif key == 'klite_codec':
            app_ver = scrape_ver_list[0].split(' ')[1]
        elif key == 'mkvtoolnix':
            app_ver = scrape_ver_list[0]
        elif key == 'obs':
            app_ver = scrape_ver_list[0].split(' ')[-1]
        elif key == 'open_shell':
            app_ver = scrape_ver_list[0]
        elif key == 'sublime_text':
            app_ver = scrape_ver_list[0].split(' ')[-1]
        elif key == 'visual_studio_code':
            app_ver = scrape_ver_list[0].split(' ')[-1][0:-1]
        elif key == 'winscp':
            app_ver = scrape_ver_list[1].split(' ')[1]
        elif key == 'python':
            app_ver = scrape_ver_list[0].split(' ')[-1]
        elif key == 'rufus':
            app_ver = scrape_ver_list[0].split(' ')[1]
        elif key == 'g_play_music':
            app_ver = scrape_ver_list[0].split(' ')[-1]
        elif key == 'java':
            app_ver = ' '.join(scrape_ver_list[0].split(' ')[1:])
        else:
            print("Something went wrong...")
            break

        # print("{}: {}".format(apps_dict[key]['app_name'], app_ver))

        # check if there is a new app version
        if app_ver != apps_dict[key]['app_local_version']:
            print("{} is outdated! There is a new version: {}".format(apps_dict[key]['app_name'], app_ver))
            get_app(app_link)

def main():
    check_apps_version()

if __name__ == '__main__':
    main()
