# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest73819(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
