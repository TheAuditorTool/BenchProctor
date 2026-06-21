# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19773(request):
    user_id = request.GET.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
