from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import os, time, sys, linecache

# textファイルからのapikeyの読み込み
apikey_file_name = 'apikey.txt'
key = linecache.getline(apikey_file_name, 1).replace('\n', '')
secret = linecache.getline(apikey_file_name, 2).replace('\n', '')
wait_time = 1

keyword = sys.argv[1]
savedir = './Data/' + keyword

flickr = FlickrAPI(key, secret, format='parsed-json')

# 検索結果のjsonを取得
result = flickr.photos.search(
    text = keyword,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, license'
)

# 検索結果から画像データを抽出
photos = result['photos']

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'

    # すでに同一ファイルが存在する場合はcontinue
    if os.path.exists(filepath): continue

    # 画像を保存
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)

print('Download',  keyword, 'images Finished.')