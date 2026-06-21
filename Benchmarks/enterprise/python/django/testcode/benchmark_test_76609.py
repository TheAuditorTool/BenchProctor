# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76609(request):
    raw_body = request.body.decode('utf-8')
    data = '{}'.format(raw_body)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
