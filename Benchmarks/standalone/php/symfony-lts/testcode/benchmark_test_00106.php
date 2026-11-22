<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00106', methods: ['POST'])]
class BenchmarkTest00106Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT name FROM users LIMIT 1');
        $data = (!empty($userInput)) ? $userInput : '';
        $stmt = $conn->prepare('SELECT * FROM users WHERE id = \'' . $data . '\'');
        $rows = $stmt->executeQuery()->fetchAllAssociative();
        return new JsonResponse(["committed" => true]);
    }
}
