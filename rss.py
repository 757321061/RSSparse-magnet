import feedparser
import re
import urllib.parse

def hash_to_magnet(hash_value):
    base_url = 'magnet:?xt=urn:btih:'
    encoded_hash = urllib.parse.quote(hash_value)
    magnet_link = base_url + encoded_hash
    return magnet_link

def get_magnet_links(rss_url, filters, excludes):
    # 解析RSS订阅
    feed = feedparser.parse(rss_url)
    magnet_links = []

    # 遍历所有的条目
    for entry in feed.entries:
        # 获取标题，并检查是否满足过滤规则和排除规则
        title = entry.get('title', '')
        if all(filter_rule in title for filter_rule in filters) and not any(exclude_rule in title for exclude_rule in excludes):
            # 提取哈希值
            enclosure = entry.get('enclosures')
            if enclosure:
                hash_value = re.search(r'/([^/]+)\.torrent', enclosure[0].get('url'))  # 修改此行
                if hash_value:
                    hash_value = hash_value.group(1)
                    magnet_link = hash_to_magnet(hash_value)
                    magnet_links.append(magnet_link)

    return magnet_links

# 替换为你的RSS订阅网址
rss_url = "https://mikanani.me/RSS/Bangumi?bangumiId=2972&subgroupid=243"

# 定义过滤规则
filters = []

# 定义排除规则
excludes = []

# 获取磁力链接
links = get_magnet_links(rss_url, filters, excludes)

# 打印磁力链接
for link in links:
    print(link)
