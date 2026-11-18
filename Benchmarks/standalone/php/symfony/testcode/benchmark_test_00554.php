<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00554', methods: ['POST'])]
class BenchmarkTest00554Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['variables']['input'] ?? '';
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $ciphertext = openssl_encrypt((string)$data, 'des-ecb', getenv('DATA_ENC_KEY'));
        return new JsonResponse(["committed" => true]);
    }
}
