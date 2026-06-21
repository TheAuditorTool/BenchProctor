# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69788(request):
    raw_body = request.body.decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
