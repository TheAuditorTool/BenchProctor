<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00529', methods: ['POST'])]
class BenchmarkTest00529Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $result = $conn->fetchAssociative('SELECT name FROM users WHERE id = ?', [$data]);
        $value = $result['name'];
        return new JsonResponse(["committed" => true]);
    }
}
