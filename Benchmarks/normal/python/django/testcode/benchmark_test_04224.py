# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest04224(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = normalise_input(origin_value)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
