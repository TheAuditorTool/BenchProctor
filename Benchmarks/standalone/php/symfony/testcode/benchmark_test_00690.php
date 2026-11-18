<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00690', methods: ['POST'])]
class BenchmarkTest00690Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $conn->executeQuery('SELECT * FROM users WHERE "' . str_replace('"', '""', (string)$data) . '" = 1');
        return new JsonResponse(["committed" => true]);
    }
}
