# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest00096(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % (referer_value,)
    requests.get(str(data))
    return JsonResponse({"saved": True})
