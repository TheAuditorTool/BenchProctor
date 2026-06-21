# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05914(request):
    xml_value = request.body.decode('utf-8')
    if not str(xml_value).isdigit():
        raise ValueError('invalid input: ' + str(xml_value))
    return JsonResponse({"saved": True})
