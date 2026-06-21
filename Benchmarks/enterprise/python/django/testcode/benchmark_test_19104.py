# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19104(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value}'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
