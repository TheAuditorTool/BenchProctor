<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00356', methods: ['POST'])]
class BenchmarkTest00356Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT name FROM users LIMIT 1');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $resp = new JsonResponse(['ok' => 1]);
        $resp->headers->setCookie(\Symfony\Component\HttpFoundation\Cookie::create('session', (string)$data, 0, '/', null, false, true, false, 'Strict'));
        return $resp;
    }
}
