<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00392', methods: ['POST'])]
class BenchmarkTest00392Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Host', '');
        $ciphertext = openssl_encrypt((string)$userInput, 'des-ecb', getenv('DATA_ENC_KEY'));
        return new JsonResponse(["committed" => true]);
    }
}
