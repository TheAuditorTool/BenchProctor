# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest47512(request):
    user_id = request.GET.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
