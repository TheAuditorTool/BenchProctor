# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68668(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header:.200s}'
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
