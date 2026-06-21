# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest08238(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
