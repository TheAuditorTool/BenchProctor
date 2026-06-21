# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63819(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
