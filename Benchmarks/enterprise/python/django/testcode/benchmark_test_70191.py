# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest70191(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % (upload_name,)
    requests.get(str(data))
    return JsonResponse({"saved": True})
