<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00020', methods: ['POST'])]
class BenchmarkTest00020Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query->get('id', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $aes = new \phpseclib3\Crypt\AES('gcm');
        $aes->setKey(hash('sha256', (string) getenv('DATA_ENC_KEY'), true));
        $aes->setNonce($nonce = random_bytes(12));
        $ciphertext = $nonce . $aes->encrypt((string)$data) . $aes->getTag();
        return new JsonResponse(["committed" => true]);
    }
}
