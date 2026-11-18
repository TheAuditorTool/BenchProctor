<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00262', methods: ['POST'])]
class BenchmarkTest00262Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $conn->executeQuery('SELECT * FROM users WHERE id = \'' . $data . '\'');
        return new JsonResponse(["committed" => true]);
    }
}
