# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest51532(request):
    user_id = request.GET.get('id', '')
    data = '%s' % str(user_id)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
