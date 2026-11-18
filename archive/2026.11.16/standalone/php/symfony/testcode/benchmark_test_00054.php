<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00054', methods: ['POST'])]
class BenchmarkTest00054Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = file_get_contents('/tmp/data');
        $conn->executeQuery('SELECT * FROM users WHERE id = ?', [$userInput]);
        return new JsonResponse(["committed" => true]);
    }
}
