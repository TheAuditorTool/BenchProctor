# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest44825(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id}'
    return HttpResponse(mark_safe('<img src="' + str(data) + '">'))
