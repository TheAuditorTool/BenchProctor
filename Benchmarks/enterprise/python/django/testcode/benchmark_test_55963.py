# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


def BenchmarkTest55963(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    processed = bleach.clean(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
