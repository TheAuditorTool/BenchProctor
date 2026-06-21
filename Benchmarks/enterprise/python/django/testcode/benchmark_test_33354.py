# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33354(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
