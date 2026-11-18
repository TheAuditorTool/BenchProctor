<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00190', methods: ['POST'])]
class BenchmarkTest00190Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT name FROM users LIMIT 1');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        unserialize($data);
        return new JsonResponse(["committed" => true]);
    }
}
