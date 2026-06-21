# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15667(request):
    host_value = request.META.get('HTTP_HOST', '')
    kind = 'json' if str(host_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = host_value
            data = parsed
        case _:
            data = host_value
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
