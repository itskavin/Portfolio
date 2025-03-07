import os
from datetime import datetime
from bs4 import BeautifulSoup

def generate_sitemap():
    domain = 'https://kavinthangavel.com'
    sitemap_path = 'sitemap.xml'
    urls = []

    for subdir, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(subdir, file)
                mod_time = os.path.getmtime(filepath)
                lastmod = datetime.utcfromtimestamp(mod_time).strftime('%Y-%m-%dT%H:%M:%SZ')
                url = os.path.join(domain, filepath.lstrip('./'))
                urls.append((url, lastmod))

    urlset = BeautifulSoup(features='xml')
    urlset.append(urlset.new_tag('urlset', xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'))

    for url, lastmod in urls:
        url_tag = urlset.new_tag('url')
        loc_tag = urlset.new_tag('loc')
        loc_tag.string = url
        lastmod_tag = urlset.new_tag('lastmod')
        lastmod_tag.string = lastmod
        url_tag.append(loc_tag)
        url_tag.append(lastmod_tag)
        urlset.urlset.append(url_tag)

    with open(sitemap_path, 'w') as f:
        f.write(urlset.prettify())

if __name__ == '__main__':
    generate_sitemap()
