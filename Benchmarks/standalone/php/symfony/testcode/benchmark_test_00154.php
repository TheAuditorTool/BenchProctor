<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00154', methods: ['POST'])]
class BenchmarkTest00154Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Origin', '');
        $data = vsprintf('%1$s', [$userInput]);
        $ciphertext = openssl_encrypt((string)$data, 'des-ecb', getenv('DATA_ENC_KEY'));
        return new JsonResponse(["committed" => true]);
    }
}
