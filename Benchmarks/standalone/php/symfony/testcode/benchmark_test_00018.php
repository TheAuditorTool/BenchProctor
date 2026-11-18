<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00018', methods: ['POST'])]
class BenchmarkTest00018Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT text FROM comments LIMIT 1');
        $data = sprintf('%s', $userInput);
        $iv = random_bytes(12);
        $tag = '';
        $_ct = openssl_encrypt((string)$data, 'aes-256-gcm', getenv('DATA_ENC_KEY'), 0, $iv, $tag);
        $ciphertext = base64_encode($iv . $tag . $_ct);
        return new JsonResponse(["committed" => true]);
    }
}
