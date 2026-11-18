# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


def BenchmarkTest00640(request):
    user_id = request.GET.get('id', '')
    data = '%s' % str(user_id)
    processed = bleach.clean(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
