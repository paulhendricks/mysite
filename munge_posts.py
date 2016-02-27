import json
import app
# from time import strftime

dat = app.post_list
for post in dat:
    datetime_obj = post['date']
    post['month'] = datetime_obj.month
    post['day'] = datetime_obj.day
    post['year'] = datetime_obj.year
    del post['date']
    del post['template']
    post['route'] = '//residentmar.io/' + post['route']

with open('./static/json/post_list.json', 'w') as outfile:
    json.dump(dat, outfile, indent=4)

xml = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
<channel>
<title>Data Hacks</title>
<link>http://www.residentmar.io/</link>
<description>Data hacks and other musings by Aleksey Bilogur</description>
"""

for post in dat:
    xml += """
        <item>
            <title>{0}</title>
            <link>{1}</link>
            <guid>{1}</guid>
            <pubdate>{2}</pubdate>
    """.format(post['title'], post['route'], str(post['year']) + '/' + str(post['month']) + '/' + str(post['day']))
    xml += """
    </item>"""

xml += """
</channel>
</rss>
"""

with open('./static/json/post_list.json', 'w') as outfile:
    json.dump(dat, outfile, indent=4)

with open('./templates/rss.xml', 'w') as outfile:
    outfile.write(xml)