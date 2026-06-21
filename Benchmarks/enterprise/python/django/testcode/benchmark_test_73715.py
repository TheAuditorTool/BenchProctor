# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest73715(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value}'
    return HttpResponse(str(data), content_type='text/html')
