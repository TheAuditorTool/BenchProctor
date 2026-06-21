# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43384(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
