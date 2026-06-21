# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest24346(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
