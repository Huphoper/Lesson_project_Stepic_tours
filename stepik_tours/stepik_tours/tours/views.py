from django.shortcuts import render
from django.views import View
from django.http import Http404, HttpResponseNotFound, HttpResponseServerError
from tours.data import departures, description, subtitle, title, tours
from random import sample


# Create your views here.
def Custom_handler404(request, exception):
    return HttpResponseNotFound('<h1>Ошибка: 404</h1>')


def Custom_handler500(request):
    return HttpResponseServerError('<h1>Ошибка: 500</h1>')


class MainView(View):
    def get(self, request, *args, **kwargs):
        # randtours = random.choices(tours, k=6)
        return render(
            request, 'index.html', context={

                'title': title,
                'subtitle': subtitle,
                'description': description,
                'departures': departures,
                'tours': sample(tours.items(), 6),
            }
        )


class DepartureView(View):
    def get(self, request, departure, *args, **kwargs):
        if departure not in departures:
            raise Http404
        filtertours = [tour for tour in tours.items() if tour[1]["departure"] == departure]
        price = [tour[1]['price'] for tour in filtertours]
        night = [tour[1]['nights'] for tour in filtertours]
        return render(
            request, 'departure.html', context={
                'title': title,
                'departurer': departures[departure],
                'departures': departures,
                'tours': filtertours,
                'len': len(filtertours),
                'maxprice': max(price),
                'minprice': min(price),
                'maxnights': max(night),
                'minnights': min(night),
            }
        )


class TourView(View):
    def get(self, request, id, *args, **kwargs):
        if id not in tours:
            raise Http404
        return render(
            request, 'tour.html', context={
                'title': title,
                'departures': departures,
                'tours': tours[id],
                'departure': departures[tours[id]['departure']]
            }
        )
