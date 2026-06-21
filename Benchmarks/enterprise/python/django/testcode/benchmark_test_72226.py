# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72226(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
