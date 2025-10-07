modelProducts = {
    'DTpres':{
        'name':'2 PVU Pressure', 'models':{'gfs'}, 'scope':{'namer'},
        'times':{
            0:[18, 24, 30], 1:[12, 18, 24, 30], 2:[12, 18, 24, 30],
            3:[12, 24], 4:[12, 24], 5:[12, 24]
        }
    },
    'pv330K':{
        'name':'330K PV', 'models':{'gfs'}, 'scope':{'namer'},
        'times':{
            0:[18, 24, 30], 1:[12, 18, 24, 30], 2:[12, 18, 24, 30],
            3:[12, 24], 4:[12, 24], 5:[12, 24]
        }
    },
    'uv250': {
        'name': '250hPa Winds + MSLP', 'models':{'gfs'}, 'scope':{'namer'},
        'times':{
            0:[18, 24, 30], 1:[12, 18, 24, 30], 2:[12, 18, 24, 30],
            3:[12, 24], 4:[12, 24], 5:[12, 24]
        }
    },
    'z500_vort': {
        'name': '500hPa Height, Vorticity', 'models':{'gfs'}, 'scope':{'namer'},
        'times':{
            0:[18, 24, 30], 1:[12, 18, 24, 30], 2:[12, 18, 24, 30],
            3:[12, 24], 4:[12, 24], 5:[12, 24]
        }
    },
    'enslows': {
        'name': 'Pressure Centers', 'models':{'gefs', 'eps'}, 'scope':{'namer'},
        'times':{3:[12, 24], 4:[12, 24], 5:[12, 24]}
    }
}