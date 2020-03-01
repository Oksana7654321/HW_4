def areYouPlayingBanjo(name):
    return '%s %s' %(name, 'plays banjo' if name[0].lower() == 'r' else 'does not play banjo')