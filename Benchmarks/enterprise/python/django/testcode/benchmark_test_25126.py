# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25126(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
