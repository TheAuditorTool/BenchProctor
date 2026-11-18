<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00341', methods: ['POST'])]
class BenchmarkTest00341Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT name FROM users LIMIT 1');
        $data = ($userInput !== null) ? $userInput : '';
        eval((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
