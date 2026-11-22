<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00105', methods: ['POST'])]
class BenchmarkTest00105Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT text FROM comments LIMIT 1');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $salt = random_bytes(16);
        $rc4 = new \phpseclib3\Crypt\RC4();
        $rc4->setKey(hash_hmac('sha256', $salt, (string) getenv('DATA_ENC_KEY'), true));
        $ciphertext = $salt . $rc4->encrypt((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
