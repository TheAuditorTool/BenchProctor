# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22171(request):
    multipart_value = request.POST.get('multipart_field', '')
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session['data'] = str(multipart_value)
    return JsonResponse({"saved": True})
