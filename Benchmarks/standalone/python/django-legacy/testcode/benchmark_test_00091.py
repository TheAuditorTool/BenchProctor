# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00091(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    code = compile(str(data), '<rule>', 'exec')
    exec(code)
    return JsonResponse({"saved": True})
