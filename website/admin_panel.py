from .pyrebase_settings import db,auth
from django.shortcuts import render, redirect


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

    # return HttpResponse(bill)
    return render(request, 'admin/analytic.html', {'coord': coord, 'severity':severity})
