# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00185(request):
    upload_name = request.FILES['upload'].name
    parts = []
    for token in str(upload_name).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
