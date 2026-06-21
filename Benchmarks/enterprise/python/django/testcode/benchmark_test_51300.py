# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64


def BenchmarkTest51300(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
