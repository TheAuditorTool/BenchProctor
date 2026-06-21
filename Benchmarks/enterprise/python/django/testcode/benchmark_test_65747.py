# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65747(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
