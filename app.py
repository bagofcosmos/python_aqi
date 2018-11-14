import urllib.request, json 

  def get_aqi(city):
      aqi_url = ("http://api.waqi.info/feed/{}/?token=ADD_YOUR_TOKEN_HERE".format(city))

      with urllib.request.urlopen(aqi_url) as url:
      scraped_data = json.loads(url.read().decode())

      data = scraped_data['data']

      for k, v in data.items():
          if k == 'aqi':
              return(v)
