<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00038', methods: ['POST'])]
class BenchmarkTest00038Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $request->headers->get('Authorization', '');
        [$data] = [$userInput, 'http'];
        $stmt = $conn->prepare('SELECT * FROM users WHERE ' . $conn->getDatabasePlatform()->quoteSingleIdentifier((string)$data) . ' = 1');
        $rows = $stmt->executeQuery()->fetchAllAssociative();
        return new JsonResponse(["committed" => true]);
    }
}
