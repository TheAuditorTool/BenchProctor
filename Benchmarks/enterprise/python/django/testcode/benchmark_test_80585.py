# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80585(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % (xml_value,)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
