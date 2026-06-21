# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11733(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return JsonResponse({"saved": True})
