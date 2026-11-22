<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00106', methods: ['POST'])]
class BenchmarkTest00106Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT name FROM users LIMIT 1');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $conn->executeQuery('SELECT * FROM users WHERE id = ?', [$data]);
        return new JsonResponse(["committed" => true]);
    }
}
