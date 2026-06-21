# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80796(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
