# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import defusedxml.ElementTree


def BenchmarkTest00280(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
