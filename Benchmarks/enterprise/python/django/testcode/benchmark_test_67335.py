# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67335(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return JsonResponse({"saved": True})
