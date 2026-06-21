# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65768(request):
    multipart_value = request.POST.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
