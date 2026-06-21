# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10504(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
