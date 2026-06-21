# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78693(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % (raw_body,)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
