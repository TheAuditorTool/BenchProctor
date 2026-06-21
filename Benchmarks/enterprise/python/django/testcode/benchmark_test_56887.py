# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56887(request):
    xml_value = request.body.decode('utf-8')
    processed = 'true' if str(xml_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
