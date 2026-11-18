<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00216', methods: ['POST'])]
class BenchmarkTest00216Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT name FROM users LIMIT 1');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $conn->executeQuery('SELECT * FROM users WHERE id = \'' . $data . '\'');
        return new JsonResponse(["committed" => true]);
    }
}
