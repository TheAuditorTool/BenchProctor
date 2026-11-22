<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00070', methods: ['POST'])]
class BenchmarkTest00070Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT name FROM users LIMIT 1');
        $data = json_decode($userInput, true)['value'] ?? '';
        $token = (string) (int) (lcg_value() * 1000000000000);
        $conn->executeStatement('UPDATE users SET reset_token = ? WHERE email = ?', [$token, (string)$data]);
        return new JsonResponse(['reset' => 'sent'], 200);
    }
}
