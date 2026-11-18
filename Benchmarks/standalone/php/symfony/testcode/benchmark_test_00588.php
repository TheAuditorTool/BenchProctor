<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00588', methods: ['POST'])]
class BenchmarkTest00588Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT name FROM users LIMIT 1');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $_coerced = (float)$data;
        $processed = $_coerced;
        eval((string)$processed);
        return new JsonResponse(["committed" => true]);
    }
}
