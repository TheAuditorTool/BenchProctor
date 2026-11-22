<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00068', methods: ['POST'])]
class BenchmarkTest00068Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('User-Agent', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $sealed = base64_decode((string)$data, true) ?: '';
        $claims = openssl_decrypt(substr($sealed, 28), 'aes-256-gcm', getenv('DATA_ENC_KEY'), OPENSSL_RAW_DATA, substr($sealed, 0, 12), substr($sealed, 12, 16));
        return new JsonResponse(["committed" => true]);
    }
}
