from io import BytesIO

import feedparser
from bs4 import BeautifulSoup
from bs4 import NavigableString
from gtts import gTTS
from pygame import mixer
from time import mktime, sleep


class WX:
    __order_days_fr = ["Conditions actuelles", "Ce soir et cette nuit", "Dimanche", "Lundi", "Mardi", "Mercredi",
                       "Jeudi", "Vendredi", "Samedi", ]
    __order_days_en = ["Current Conditions", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                     "Saturday", ]

    def __init__(self, message: str = None, lang: str = None):
        self.url = None
        mixer.init()

        self.d_weather = {
            "timestamp": 0
        }

        if message:
            self.message = {
                "text": message,
                "audio": self.__build_audio(message, lang)
            }
        else:
            self.message = None


    def __build_audio(self, message: str, lang: str):
        lang = lang.split("-")
        ram_file = BytesIO()
        tts = gTTS(text=message, lang=lang[0], tld=lang[1])
        tts.write_to_fp(ram_file)
        ram_file.seek(0)
        audio = mixer.Sound(ram_file)
        ram_file.close()
        return audio

    def get_weather_report(self, url: str = None):
        if self.url is None and url is not None:
            self.url = url
        elif self.url is not None:
            url = self.url
        else:
            raise Exception("url is required")

        rss = feedparser.parse(url)
        d_weather = {
            "title": {"text": rss["feed"]["title"],
                      "audio": self.__build_audio(rss["feed"]["title"], rss["feed"]["language"])},
            "lang": rss["feed"]["language"],
            "timestamp": mktime(rss["feed"]["updated_parsed"])
        }

        if d_weather["timestamp"] > self.d_weather["timestamp"]:
            for entry in rss["entries"]:
                html = BeautifulSoup(entry["summary"], "html.parser")
                for br in html.find_all("br"):
                    br.replace_with(NavigableString(";"))

                d_weather[entry["title"].split(":")[0]] = {"text": html.get_text()}
                d_weather[entry["title"].split(":")[0]]["audio"] = self.__build_audio(html.get_text(), d_weather["lang"])

            self.d_weather = d_weather

        return rss

    def playback(self):
        if self.message:
            self.message["audio"].play()
            while mixer.get_busy():
                sleep(0.1)

        self.d_weather["title"]["audio"].play()
        while mixer.get_busy():
            sleep(0.1)

        for key in self.d_weather:
            if key not in ["timestamp", "title", "lang"]:
                self.d_weather[key]["audio"].play()
                while mixer.get_busy():
                    sleep(0.1)


def main():
    message_fr = (
        "Ici radio météo Canada, opérant sur la fréquence 162,550 MHz. Le service est assuré par une communauté bénévole opérant la station V E 2 T M Q. Pour informations communiquez à: W X @ V E 2 T M Q point C A",
        "fr-ca")
    rss_fr = "https://meteo.gc.ca/rss/weather/45.529_-73.562_f.xml"
    wx_fr = WX(*message_fr)
    wx_fr.get_weather_report(rss_fr)

    message_en = (
        "This is Weather Radio Canada, operating on frequency 162.550 MHz. The service is provided by a volunteer community operating station V E 2 T M Q. For information, contact: W X @ V E 2 T M Q dot C A.",
        "en-ca")
    rss_en = "https://meteo.gc.ca/rss/weather/45.529_-73.562_e.xml"
    wx_en = WX(*message_en)
    wx_en.get_weather_report(rss_en)

    return wx_fr, wx_en