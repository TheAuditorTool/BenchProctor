# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02938(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    prefix = ''
    data = prefix + str(auth_header)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
