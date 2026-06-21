# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31010(request):
    upload_name = request.FILES['upload'].name
    data = '{}'.format(upload_name)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
