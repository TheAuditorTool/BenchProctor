<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00041', methods: ['POST'])]
class BenchmarkTest00041Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = (new \Redis())->get('user_data');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $conn->executeQuery('SELECT * FROM users WHERE ' . $conn->getDatabasePlatform()->quoteSingleIdentifier((string)$data) . ' = 1');
        return new JsonResponse(["committed" => true]);
    }
}
