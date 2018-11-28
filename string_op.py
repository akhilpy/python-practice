

def url_friendly(title):
    if '/' in title:
         title=title.replace('/', '-')

    if ' ' in title:
         title=title.replace(' ', '-')
    
    if '_' in title:
         title=title.replace('_', '-')

    return title.lower()
         


print(url_friendly("abc_FDE"))