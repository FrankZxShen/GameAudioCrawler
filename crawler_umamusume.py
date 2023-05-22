# @Time    : 2021/12/16 7:15
# @Author  : 南黎
# @FileName: 爬取音乐程序.py


# 测试时如果发现歌曲地址解析得到的不是自己想要的歌曲，可能是因为你没有刷新网页的解析结果导致！
# 这些地址仅供学习参考，会随时间过期，授人以鱼不如授人以渔

# 免费歌曲（以下地址有部分会随时间变化，主要是提供一个思路）
# 金玉良缘 歌曲播放地址：http://www.kuwo.cn/play_detail/196835141
# 金玉良缘 歌曲播放id： 196835141
# 金玉良缘 歌曲MP3地址的存放地址： http://www.kuwo.cn/api/v1/www/music/playUrl?mid=196835141&type=music&httpsStatus=1&reqId=66231ca1-5e04-11ec-96d1-d1bbc17ab269
# 金玉良缘 歌曲MP3地址： https://other-web-nf01-sycdn.kuwo.cn/593dddbc7e2c3d8e42c3ad0349ec219b/61ba83b5/resource/n3/68/45/237017447.mp3

# 收费歌曲
# 你会发现无法获取到网页的playurl
# 黄昏 歌曲播放地址：http://www.kuwo.cn/play_detail/1044318
# 黄昏 歌曲播放id： 1044318
# 黄昏 歌曲MP3地址的原来的存放地址： http://www.kuwo.cn/api/v1/www/music/playUrl?mid=1044318&type=music&httpsStatus=1&reqId=66231ca1-5e04-11ec-96d1-d1bbc17ab269
# 黄昏 歌曲MP3地址的修改后存放地址： https://www.kuwo.cn/api/v1/www/music/playUrl?mid=1044318&type=mp3&httpsStatus=1&reqId=66231ca1-5e04-11ec-96d1-d1bbc17ab269
# 黄昏 歌曲MP3地址： https://other-web-ra01-sycdn.kuwo.cn/9613a15eacfc54710a0762b566b3235a/61ba850e/resource/n2/128/98/58/4249925507.mp3

# 1.看响应参数是不是200判断url是否能访问
import time
import requests
print("1.看响应参数是不是200判断url是否能访问")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
    'csrf': 'RUJ53PGJ4ZD',
    'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1577029678,1577034191,1577034210,1577076651; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1577080777; kw_token=RUJ53PGJ4ZD'
}
response = requests.get(
    "https://other-web-ra01-sycdn.kuwo.cn/1647fce2c2c049bf4ef8462545763e61/61ba7d80/resource/n2/128/98/58/4249925507.mp3", headers=headers)
print(response)

# 2.试着根据黄昏音乐MP3地址url解析成功的结果下载一首音乐，存放在本程序目录下
print("2.试着根据音乐MP3地址url解析成功的结果下载一首音乐，存放在本程序目录下")
# 注意这里的url会随时间过期变化，你要通过前面的教程自己手动获取！
with open("下载的一首歌曲.mp3", "wb") as file:
    url = "https://other-web-ra01-sycdn.kuwo.cn/1647fce2c2c049bf4ef8462545763e61/61ba7d80/resource/n2/128/98/58/4249925507.mp3"
    music = requests.get(url)  # 获取解析到的数据
    file.write(music.content)  # 把数据写入缓冲区文件
    file.flush()  # 把数据存入缓冲区
    file.close()  # 关闭文件

# 3.输入一首歌曲的地址（不是MP3地址），解析得到音乐,完整项目
print("3.输入一首歌曲的地址（不是MP3地址），解析得到音乐")


def get_mp3_name():
    data_time = time.strftime(
        '%Y-%m-%d-%H-%M-%S', time.localtime())  # 格式化获取的当地时间
    mp3_name = data_time+".mp3"
    return mp3_name


def downMusic(url):
    # 该网站有反爬机制，要模拟浏览器来进行伪装。
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
        'csrf': 'RUJ53PGJ4ZD',
        'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1577029678,1577034191,1577034210,1577076651; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1577080777; kw_token=RUJ53PGJ4ZD'
    }

    # 假设url是http://www.kuwo.cn/play_detail/196835141，得到mid196835141
    mid = url.split("/")[-1]
    # 把得到的mid参数填入指定位置得到了存放MP3文件地址的json地址
    save_mp3_url = "http://www.kuwo.cn/api/v1/www/music/playUrl?mid=%s&type=mp3&httpsStatus=1&reqId=66231ca1-5e04-11ec-96d1-d1bbc17ab269" % mid
    mp3_response = requests.get(
        save_mp3_url, headers=headers)  # 解析存放MP3文件地址的json地址
    mp3_url = mp3_response.json().get("data").get(
        "url")  # 根据解析存放MP3文件地址的json地址的内容，获取MP3地址
    with open(get_mp3_name(), "wb") as file:
        music = requests.get(mp3_url, headers=headers)  # 获取解析到的数据
        file.write(music.content)  # 把数据写入缓冲区文件
        file.flush()  # 把数据存入缓冲区
        file.close()  # 关闭文件


url = input("输入一首歌曲的播放地址下载歌曲:")
downMusic(url)
