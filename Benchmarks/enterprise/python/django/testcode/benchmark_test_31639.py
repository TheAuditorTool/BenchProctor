# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31639(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return JsonResponse({"saved": True})
