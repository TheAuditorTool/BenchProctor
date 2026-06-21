# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest41097(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
