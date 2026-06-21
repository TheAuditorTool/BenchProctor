# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59864(request):
    multipart_value = request.POST.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
