from .pyrebase_settings import db,auth
from django.shortcuts import render, redirect
import pandas

def analytic(request):
    results = db.child('Zones').get()
    severity = {'urgent':10,'high':25,'normal':70,'low':40}
    data = results.val()
    coord = []
    for i in data:
        try:
            lat = data[i]['zoneLat']
            long = data[i]['zoneLong']
            coord.append([lat, long])
        except:
            pass
        try:
            severity[data[i]['severity']]+=1
        except:
            pass


    severity = [severity['urgent'],severity['high'],severity['normal'],severity['low']]

    print(coord)


    df = pandas.read_csv('accidentnews/road.csv')
    print(df)

    state = df['State'].values

    years = []
    label = []
    for i in df['2003']:
        years.append([])

    for i in df:
        if i != "State":
            label.append(i)
        for j,k in enumerate(df[i]):
            years[j].append(k)

    for i,j in enumerate(years):
        years[i] = ','.join(map(str, j))

    # label = df['State'].values

    # print(df['State'].values)
    # # context['label'] = []
    # # for i in df['State']:
    # #   context['label'].append(i)

    # labels = []
    # for i in df.keys():
    #     if i != "State":
    #         labels.append(i)

    # years = []
    # for i in df['State']:
    #     years.append(str(i)+','+','.join(map(str, df[i]))) 

    return render(request, 'adm/analytic.html', {'coord': coord, 'severity':severity, 'label':label,'state':state, 'years':years})

