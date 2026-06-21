# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest43497(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
