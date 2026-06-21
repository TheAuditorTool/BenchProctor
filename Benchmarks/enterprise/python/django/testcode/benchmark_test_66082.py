# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66082(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
