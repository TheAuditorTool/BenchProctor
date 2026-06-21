# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24232(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
