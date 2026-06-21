# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35080(request):
    multipart_value = request.POST.get('multipart_field', '')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(multipart_value))
    return JsonResponse({"saved": True})
