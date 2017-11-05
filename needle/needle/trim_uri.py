def trim_uri(link):
    count = len(link)
    uri = ''
    while link[count - 1] != '/':
        uri = link[count - 1] + uri
        count = count - 1
    return(uri)
