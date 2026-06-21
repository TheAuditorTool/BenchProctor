# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23384(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % (xml_value,)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
