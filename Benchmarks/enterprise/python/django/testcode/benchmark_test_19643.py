# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19643(request):
    upload_name = request.FILES['upload'].name
    data, _sep, _rest = str(upload_name).partition('\x00')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
