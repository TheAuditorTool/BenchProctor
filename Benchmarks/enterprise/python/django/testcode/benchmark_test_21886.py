# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21886(request):
    user_id = request.GET.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
