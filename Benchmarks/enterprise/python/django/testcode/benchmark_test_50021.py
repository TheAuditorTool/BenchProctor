# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest50021(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    return HttpResponse(str(data), content_type='text/html')
