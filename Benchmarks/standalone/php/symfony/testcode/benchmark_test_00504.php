<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00504', methods: ['POST'])]
class BenchmarkTest00504Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $result = $conn->fetchAssociative('SELECT name FROM users WHERE id = ?', [$data]);
        if ($result === false) { return new JsonResponse(["error" => "not found"], 404); }
        $value = $result['name'];
        return new JsonResponse(["committed" => true]);
    }
}
