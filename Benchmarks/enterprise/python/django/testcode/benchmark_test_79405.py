# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest79405(request):
    user_id = request.GET.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
