<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00051', methods: ['POST'])]
class BenchmarkTest00051Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT name FROM users LIMIT 1');
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        $aes = new \phpseclib4\Crypt\AES('gcm');
        $aes->setKey(hash('sha256', (string) getenv('DATA_ENC_KEY'), true));
        $aes->setNonce($nonce = random_bytes(12));
        $ciphertext = $nonce . $aes->encrypt((string)$data) . $aes->getTag();
        return new JsonResponse(["committed" => true]);
    }
}
