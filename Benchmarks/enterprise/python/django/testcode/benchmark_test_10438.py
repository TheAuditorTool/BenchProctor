# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10438(request):
    user_id = request.GET.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
