# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00070(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    request.session.update({'data': str(data)})
    return JsonResponse({"saved": True})
