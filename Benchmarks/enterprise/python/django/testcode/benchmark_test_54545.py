# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54545(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
