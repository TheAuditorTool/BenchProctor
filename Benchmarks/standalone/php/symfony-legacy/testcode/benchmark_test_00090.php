<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00090', methods: ['POST'])]
class BenchmarkTest00090Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        $sealed = base64_decode((string)$data, true) ?: '';
        $claims = openssl_decrypt(substr($sealed, 28), 'aes-256-gcm', getenv('DATA_ENC_KEY'), OPENSSL_RAW_DATA, substr($sealed, 0, 12), substr($sealed, 12, 16));
        return new JsonResponse(["committed" => true]);
    }
}
