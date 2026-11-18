<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00691', methods: ['POST'])]
class BenchmarkTest00691Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT bio FROM profiles LIMIT 1');
        $conn->executeQuery('SELECT * FROM users WHERE id = \'' . $userInput . '\'');
        return new JsonResponse(["committed" => true]);
    }
}
