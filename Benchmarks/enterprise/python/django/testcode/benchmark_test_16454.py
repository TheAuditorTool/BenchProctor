# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16454(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value}'
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
