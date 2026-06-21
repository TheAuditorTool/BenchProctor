# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest12522(request):
    user_id = request.GET.get('id', '')
    data = '%s' % str(user_id)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
