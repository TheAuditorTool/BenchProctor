# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00158(request):
    xml_value = request.body.decode('utf-8')
    code = compile(str(xml_value), '<rule>', 'exec')
    exec(code)
    return JsonResponse({"saved": True})
