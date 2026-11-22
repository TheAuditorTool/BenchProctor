# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Hash import MD4


def BenchmarkTest00066(request):
    user_id = request.GET.get('id', '')
    kind = 'json' if str(user_id).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(user_id).strip()
        case _:
            data = str(user_id)
    digest = MD4.new(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
