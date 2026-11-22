<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00212', methods: ['POST'])]
class BenchmarkTest00212Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = getenv('APP_INPUT') ?: '';
        [$data] = [$userInput, 'http'];
        $token = (string) (int) (lcg_value() * 1000000000000);
        $conn->executeStatement('UPDATE users SET reset_token = ? WHERE email = ?', [$token, (string)$data]);
        return new JsonResponse(['reset' => 'sent'], 200);
    }
}
