<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00643', methods: ['POST'])]
class BenchmarkTest00643Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $iv = random_bytes(12);
        $tag = '';
        $_ct = openssl_encrypt((string)$data, 'aes-256-gcm', getenv('DATA_ENC_KEY'), 0, $iv, $tag);
        $ciphertext = base64_encode($iv . $tag . $_ct);
        return new JsonResponse(["committed" => true]);
    }
}
