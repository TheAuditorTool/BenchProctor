# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27264(request):
    raw_body = request.body.decode('utf-8')
    data = '{}'.format(raw_body)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
