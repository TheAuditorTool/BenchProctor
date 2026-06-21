# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33088(request):
    raw_body = request.body.decode('utf-8')
    data = '{}'.format(raw_body)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
