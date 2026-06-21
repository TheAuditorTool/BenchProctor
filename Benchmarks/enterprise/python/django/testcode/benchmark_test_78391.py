# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78391(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = f'{header_value:.200s}'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
