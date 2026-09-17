import io, json
tpl = io.open('template.html', encoding='utf-8').read()
data = io.open('roster.json', encoding='utf-8').read().strip()
json.loads(data)                      # fail loudly on bad data
assert '__DATA__' in tpl
page = tpl.replace('__DATA__', data, 1)
head = ('<!doctype html><html><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="robots" content="noindex,nofollow,noarchive,noimageindex">'
        '<meta name="googlebot" content="noindex,nofollow">'
        '<meta name="referrer" content="no-referrer">'
        '<meta name="color-scheme" content="light dark">'
        '</head><body>\n')
io.open('index.html','w',encoding='utf-8').write(head + page + '\n</body></html>\n')
print('built index.html', round(len(page)/1024), 'KB')
