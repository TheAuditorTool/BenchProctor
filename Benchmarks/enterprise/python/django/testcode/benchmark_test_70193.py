# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from urllib.parse import urlparse


def BenchmarkTest70193(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return redirect(str(target_url))
