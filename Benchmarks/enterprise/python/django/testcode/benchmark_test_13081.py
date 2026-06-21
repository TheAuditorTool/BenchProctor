# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13081(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % (xml_value,)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
