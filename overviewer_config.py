def signFilter(poi):
    if poi['id'] == 'Sign':
        return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "http://overviewer.org/avatar/%s" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']

worlds["glowstone"] = "~/tmp/TSCraft"

renders["day"] = {
    "world": "glowstone",
    "title": "Daytime",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
    'markers': [dict(name="Signs", filterFunction=signFilter), dict(name="Players", filterFunction=playerIcons)],
}

defaultzoom = 1

outputdir = "${OUTPUT_DIR}"
