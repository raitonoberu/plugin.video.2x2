import xbmcgui
import xbmcplugin
import xbmcaddon
import requests

api_url = "https://uma.media/api/play/options/dcab9b90a33239837c0f71682d6606da/?format=json"
resolutions = ["1280x720", "1024x576", "640x360"]

addon = xbmcaddon.Addon()

response = requests.get(api_url, headers={"Referer": "https://online.2x2tv.ru/"})
if response:
    hls_url = response.json()["live_streams"]["hls"][0]["url"]
    playlist = requests.get(hls_url).text
    streams = list(filter(lambda i: i.startswith("http"), playlist.split("\n")))
    number_of_servers = len(streams) / len(resolutions)
    for i in range(len(streams)):
        item = xbmcgui.ListItem("2x2 " + resolutions[int(i / number_of_servers)])
        xbmcplugin.addDirectoryItem(int(sys.argv[1]), streams[i], item, isFolder=0)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
else:
    dialog = xbmcgui.Dialog()
    ok = dialog.ok("Error", "{0}: {1}".format(response.status_code, response.json()['detail']['languages'][-1]['title'].encode('utf-8')))
