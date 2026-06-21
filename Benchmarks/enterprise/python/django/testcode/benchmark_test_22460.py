# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22460(request):
    user_id = request.GET.get('id', '')
    data = '%s' % (user_id,)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
