<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00110', methods: ['POST'])]
class BenchmarkTest00110Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $request->headers->get('Authorization', '');
        $data = base64_decode($userInput);
        $stmt = $conn->prepare('SELECT * FROM users WHERE id = \'' . $data . '\'');
        $rows = $stmt->executeQuery()->fetchAllAssociative();
        return new JsonResponse(["committed" => true]);
    }
}
