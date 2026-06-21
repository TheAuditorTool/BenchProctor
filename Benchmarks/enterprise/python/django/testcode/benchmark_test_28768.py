# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest28768(request):
    host_value = request.META.get('HTTP_HOST', '')
    allowed = {'config.json', 'index.html', 'readme.md'}
    if host_value not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + host_value
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
