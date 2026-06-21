# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from django.http import HttpResponse


def BenchmarkTest33567(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    return HttpResponse(str(data), content_type='text/html')
