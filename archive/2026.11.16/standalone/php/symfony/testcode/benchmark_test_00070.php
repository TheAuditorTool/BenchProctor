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
        $userInput = $conn->fetchOne('SELECT text FROM comments LIMIT 1');
        $digest = hash('sha256', (string)$userInput);
        return new JsonResponse(["committed" => true]);
    }
}
