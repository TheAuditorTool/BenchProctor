# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest29843(request):
    user_id = request.GET.get('id', '')
    data = '%s' % (user_id,)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
