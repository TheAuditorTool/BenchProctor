<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00090', methods: ['POST'])]
class BenchmarkTest00090Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Referer', '');
        $salt = random_bytes(16);
        $rc4 = new \phpseclib4\Crypt\RC4();
        $rc4->setKey(hash_hmac('sha256', $salt, (string) getenv('DATA_ENC_KEY'), true));
        $ciphertext = $salt . $rc4->encrypt((string)$userInput);
        return new JsonResponse(["committed" => true]);
    }
}
