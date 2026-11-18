<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00233', methods: ['POST'])]
class BenchmarkTest00233Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT text FROM comments LIMIT 1');
        $data = vsprintf('%1$s', [$userInput]);
        $result = $conn->fetchAssociative('SELECT name FROM users WHERE id = ?', [$data]);
        $value = $result['name'];
        return new JsonResponse(["committed" => true]);
    }
}
