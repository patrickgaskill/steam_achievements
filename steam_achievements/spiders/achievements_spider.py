import scrapy
import json
from steam_achievements.items import App, AchievementPercentage

STEAM_API = "http://api.steampowered.com"
GET_APP_LIST_URL = "{}/ISteamApps/GetAppList/v0002/".format(STEAM_API)
GET_GLOBAL_ACHIEVEMENT_PERCENTAGES_FOR_APP_URL = "{}/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/".format(
    STEAM_API)


class AchievementsSpider(scrapy.Spider):
    name = "achievements"

    start_urls = [GET_APP_LIST_URL]

    def parse(self, response):
        apps = json.loads(response.body)['applist']['apps']
        for app in apps:
            yield App(app)
            appid = app['appid']
            percentages_url = "{url}?gameid={appid}".format(
                url=GET_GLOBAL_ACHIEVEMENT_PERCENTAGES_FOR_APP_URL, appid=appid)
            yield scrapy.Request(percentages_url, callback=self.achievement_percentages_parse, meta={'appid': appid})

    def achievement_percentages_parse(self, response):
        print(response)
        achievements = json.loads(response.body)[
            'achievementpercentages']['achievements']
        for achievement in achievements:
            yield AchievementPercentage(achievement, appid=response.meta['appid'])
