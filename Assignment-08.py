import os, requests, bs4, datetime, shelve, re


[docs]def get_soup(url_arg: str) -> bs4.BeautifulSoup:

    print(f'Downloading page {url_arg}...')
    res = requests.get(url_arg)
    res.raise_for_status()
    return bs4.BeautifulSoup(res.text, 'lxml')



[docs]def compare_timestamps(timestamp_arg: str, shelf_arg: shelve.open, url_arg: str) -> bool:

    comic_date = datetime.datetime.strptime(timestamp_arg, '%B %d, %Y').date()
    shelf_date = shelf_arg[url_arg]
    if comic_date > shelf_date:  # New comic available, download comic
        return True
    return False



[docs]def check_key(shelf_arg: shelve.open, url_arg: str) -> bool:

    keys = shelf_arg.keys
    if url_arg in keys:
        return True
    return False



[docs]def save_comic(comic_url_arg: str, shelf_arg: shelve.open, url_arg: str) -> None:
    
    print(f'Downloading image {comic_url_arg}...')
    comic_res = requests.get(comic_url_arg)
    comic_res.raise_for_status()

    # Save the comic to desktop.
    image_file = open(os.path.join(os.path.expanduser('~/Desktop'), os.path.basename(comic_url_arg)), "wb")
    for chunk in comic_res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    now = datetime.datetime.now().date()
    shelf_arg[url_arg] = now
    return None



[docs]def main():
    comic_shelf = shelve.open('comic')

    # Download page
    url = 'http://www.lefthandedtoons.com/'
    soup = get_soup(url)

    # Get comic url in case it needs to be downloaded
    image_elem = soup.select('.comicimage')
    comic_url = image_elem[0].get('src')

    # Compare page's timestamp to shelve's
    comic_title_elem = soup.select('.comictitlearea')
    if not comic_title_elem:
        print('Could not find comic timestamp.')
    else:
        title_text = comic_title_elem[0].getText()
        match = re.search('\w+ \d+, \d{4}', title_text)
        if not check_key(comic_shelf, url) or compare_timestamps(match.group(), comic_shelf, url):
            save_comic(comic_url, comic_shelf, url)

    # Download page
    url = 'http://buttersafe.com/'
    soup = get_soup(url)

    # Get comic url in case it needs to be downloaded
    div_elem = soup.find('div', attrs={'id': 'comic'})
    comic_url = div_elem.find('img')['src']

    # Compare page's timestamp to shelve's
    comic_header = soup.select('#headernav-date')
    if not comic_header:
        print('Could not find comic timestamp.')
    else:
        header_text = comic_header[0].getText()
        match = re.search('(\w+), (\w+) (\d+).., (\d{4})', header_text)
        comic_timestamp = f'{match.group(2)} {match.group(3)}, {match.group(4)}'
        if not check_key(comic_shelf, url) or compare_timestamps(comic_timestamp, comic_shelf, url):
            save_comic(comic_url, comic_shelf, url)

    comic_shelf.close()



if __name__ == '__main__':
    main()