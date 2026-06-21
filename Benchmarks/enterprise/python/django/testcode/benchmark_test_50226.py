# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50226(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
