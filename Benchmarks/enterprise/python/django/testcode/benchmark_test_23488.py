# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest23488(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    return HttpResponse(str(data), content_type='text/html')
