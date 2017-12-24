# -*- coding: utf-8 -*-
# import os
import scrapy
import pdb
import datetime, time
import re
import json

# 限制更新时间 ，大于该秒数就不更新了
limit_update_time = 250000

# 单场比赛 item
class match_Item(scrapy.Item):
    league_id = scrapy.Field()  # 联赛ID
    match_id = scrapy.Field()   # 比赛唯一ID
    team_id = scrapy.Field()    # 队伍ID
    home_id = scrapy.Field()    # 主队ID
    home_name = scrapy.Field()  # 主队名称
    away_id = scrapy.Field()    # 客队ID
    away_name = scrapy.Field()    # 客队名称
    match_result = scrapy.Field()   # 比赛结果  3：主胜 1：平局 0：主负
    match_time = scrapy.Field()     # 开赛时间
    match_score = scrapy.Field()    # 比分
    match_players = scrapy.Field()   # 队伍首发球员列表

class SoccerSpider(scrapy.Spider):
    name = 'teams'
    allowed_domains = ['http://www.tzuqiu.cc/']
    nowadays = datetime.datetime.now().strftime("%Y-%m-%d")  # 获取当前日期
    # tomorrow = (datetime.datetime.now()+datetime.timedelta(days = +1)).strftime("%Y-%m-%d")     # 获取明天日期
    # 生成遍历的日期列表
    start_urls = ['http://www.tzuqiu.cc/']
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url)

    # 首页找到联赛页面url
    def parse(self, response):
        for li in response.xpath("//div[@id='competition-league-list']/ul/li"):
            league_url = 'http://www.tzuqiu.cc'+li.xpath('a/@href').extract()[0]
            yield scrapy.Request(league_url, meta={}, callback=self.league_parse, dont_filter = True)

    # 获取联赛列表
    def league_parse(self, response):
        handle_httpstatus_list = [404]
        if response.status in handle_httpstatus_list:
            print('访问404')
            return False
        for tr in response.css('table[id=rankTable0]').xpath('tbody/tr'):
            team_id = tr.xpath('td')[1].xpath('a/@href').extract()[0].split('/')[2]
            team_fixture_url = 'http://www.tzuqiu.cc/teams/'+team_id+'/fixture.do'
            yield scrapy.Request(team_fixture_url, meta={'team_id':team_id}, callback=self.team_parse, dont_filter = True)

    # 获取队伍列表
    def team_parse(self, response):
        team_id = response.meta['team_id']
        for tr in response.css('tbody[id=fixture-body]').xpath('tr'):
            not_end = tr.xpath('td')[6].xpath('text()').extract()[0].strip() == 'vs'
            if not_end: continue  # 如果没有结束就跳过
            # 如果已经比当前时间早了设定时间就跳过，提高更新数据速度
            match_time = tr.xpath('td')[3].xpath('text()').extract()[0]
            start_time_array = time.strptime(match_time, "%Y-%m-%d")
            start_time_stamp = time.mktime(start_time_array)
            now_time_stamp = time.time()
            if (now_time_stamp - start_time_stamp) > limit_update_time:
                continue
            # 结束

            match_id = tr.css('::attr(matchid)').extract()[0]
            league_id = tr.css('::attr(competitionid)').extract()[0]
            home_id = tr.css('::attr(hometeamid)').extract()[0]
            away_id = tr.css('::attr(awayteamid)').extract()[0]
            try:
                match_score = tr.xpath('td')[6].xpath('a/text()').extract()[0]
            except:
                print('获取比分出错')
                pdb.set_trace()
            match_result = ''   # 比赛结果 3 主胜 1 平局 0 主负
            result_a = tr.xpath('td')[1].xpath('a')
            if len(result_a) == 0:
                return False
            try:
                home_goal_text = match_score.split(':')[0].strip()
                away_goal_text = match_score.split(':')[1].strip()
                if home_goal_text[0] == '*':
                    home_goal = float(home_goal_text[1:])
                else:
                    home_goal = float(home_goal_text)
                if away_goal_text[-1] == '*':
                    away_goal = float(away_goal_text[:-1])
                else:
                    away_goal = float(away_goal_text)
            except:
                print('转化进球数出错')
                pdb.set_trace()
            if home_goal > away_goal:
                match_result = 3
            elif home_goal == away_goal:
                match_result = 1
            elif home_goal < away_goal:
                match_result = 0
            home_name = tr.xpath('td')[4].xpath('a/text()').extract()[0]
            away_name = tr.xpath('td')[8].xpath('a/text()').extract()[0]
            detail_url = 'http://www.tzuqiu.cc' + tr.xpath('td')[6].xpath('a/@href').extract()[0]
            meta_dice = {}
            meta_dice['team_id'] = team_id  # 当前查询的球队id
            meta_dice['match_id'] = match_id
            meta_dice['league_id'] = league_id
            meta_dice['home_id'] = home_id
            meta_dice['away_id'] = away_id
            meta_dice['match_result'] = match_result
            meta_dice['match_time'] = match_time
            meta_dice['home_name'] = home_name
            meta_dice['match_score'] = match_score
            meta_dice['away_name'] = away_name
            yield scrapy.Request(detail_url, meta=meta_dice, callback=self.detail_parse, dont_filter = True)

    def detail_parse(self, response):
        team_id = response.meta['team_id']
        match_id = response.meta['match_id']
        league_id = response.meta['league_id']
        home_id = response.meta['home_id']
        away_id = response.meta['away_id']
        match_result = response.meta['match_result']
        match_time = response.meta['match_time']
        home_name = response.meta['home_name']
        match_score = response.meta['match_score']
        away_name = response.meta['away_name']
        # 判断是主场还是客场
        team_is_home = True
        if team_id == away_id:
            team_is_home = False


        # 对已经结束的比赛才进行读取信息
        is_end = False
        match_status_text = response.css('td[class=match-info]').xpath('div/table/tr')[1].xpath('td')[1].xpath('text()').extract()[0].strip()
        if match_status_text == '已结束':
            is_end = True
        if not is_end:
            return False
        first_player_list = []  # 记录本队伍该场比赛的首发球员列表
        for script in response.xpath('//script'):
            # 当没有type时才可能是json
            if len(script.xpath('@type')) == 0:
                # 将比赛细节数据列表保存下来
                # 根据本队主客场的不同查找不同数据
                if team_is_home:
                    detail_info = re.findall(r"homePlayerStatistics = \[\{.*}]", script.xpath('text()').extract()[0])
                    search_text = 'homePlayerStatistics = '
                else:
                    detail_info = re.findall(r"awayPlayerStatistics = \[\{.*}]", script.xpath('text()').extract()[0])
                    search_text = 'awayPlayerStatistics = '
                if len(detail_info) != 0:
                    # match_detail存储的是球员列表
                    match_detail = json.loads(detail_info[0].replace(search_text,''))
                    # for 循环遍历每个球员，根据其中teamId, 区分队伍
                    for player in match_detail:
                        # 记录球员信息的字典:
                        team_player_dice = {}
                        team_player_dice['teamId'] = str(player['teamId'])  # 队伍id
                        team_player_dice['isFirstEleven'] = player['isFirstEleven']  # 是否是首发
                        # 只记录当前查询球队的球员信息
                        if team_player_dice['teamId'] == team_id and team_player_dice['isFirstEleven']:
                            team_player_dice['playerId'] = str(player['playerId'])  # 球员id
                            team_player_dice['playerName'] = player['playerName']  # 球员名称
                            try:
                                team_player_dice['shirtNo'] = str(player['shirtNo'])  # 球员编号 这个可能没有
                            except:
                                team_player_dice['shirtNo'] = ''
                            team_player_dice['currentMarketValue'] = str(player['player']['currentMarketValue'])  # 球员当前身价
                            team_player_dice['matchId'] = str(player['matchId'])  # 比赛id
                            try:
                                team_player_dice['position'] = player['position'].strip()  # 所担任位置 这个可能没有 可以用['player']['mainposition']
                            except:
                                team_player_dice['position'] = player['player']['mainPosition'].strip()
                            try:
                                team_player_dice['rate'] = str(player['rate'])  # 评分 这个可能没有
                            except:
                                team_player_dice['rate'] = ''
                            first_player_list.append(team_player_dice)
        # 将数据保存到数据模型中
        single_match_Item = match_Item()
        single_match_Item['league_id'] = league_id  # 联赛ID
        single_match_Item['match_id'] = match_id  # 比赛唯一ID
        single_match_Item['team_id'] = team_id  # 队伍ID
        single_match_Item['home_id'] = home_id  # 主队ID
        single_match_Item['home_name'] = home_name  # 主队名称
        single_match_Item['away_id'] = away_id  # 客队ID
        single_match_Item['away_name'] = away_name  # 客队名称
        single_match_Item['match_result'] = match_result  # 比赛结果  3：主胜 1：平局 0：主负
        single_match_Item['match_time'] = match_time  # 开赛时间
        single_match_Item['match_score'] = match_score  # 比分
        single_match_Item['match_players'] = first_player_list  # 队伍首发球员列表  有可能没有，这时len小于110就直接返回
        if len(first_player_list) < 11:
            return False
        yield single_match_Item





