<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00071', methods: ['POST'])]
class BenchmarkTest00071Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $aes = new \phpseclib4\Crypt\AES('gcm');
        $aes->setKey(hash('sha256', (string) getenv('DATA_ENC_KEY'), true));
        $aes->setNonce($nonce = random_bytes(12));
        $ciphertext = $nonce . $aes->encrypt((string)$data) . $aes->getTag();
        return new JsonResponse(["committed" => true]);
    }
}
