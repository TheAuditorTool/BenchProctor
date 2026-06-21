# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08286(request):
    user_id = request.GET.get('id', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(user_id))
    return JsonResponse({"saved": True})
