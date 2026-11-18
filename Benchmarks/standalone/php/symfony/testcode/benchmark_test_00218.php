<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00218', methods: ['POST'])]
class BenchmarkTest00218Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT name FROM users LIMIT 1');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $_coerced = (float)$data;
        $processed = $_coerced;
        eval((string)$processed);
        return new JsonResponse(["committed" => true]);
    }
}
