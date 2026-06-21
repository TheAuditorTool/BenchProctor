# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest08599(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id}'
    return HttpResponse(str(data), content_type='text/html')
