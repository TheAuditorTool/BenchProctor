# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest73051(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % (xml_value,)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
