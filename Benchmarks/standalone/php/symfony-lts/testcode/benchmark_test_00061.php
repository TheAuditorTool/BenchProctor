<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00061', methods: ['POST'])]
class BenchmarkTest00061Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $request->headers->get('Referer', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $_coerced = (int)$data;
        $parsedId = $_coerced;
        $stmt = $conn->prepare('SELECT * FROM users WHERE id = \'' . $parsedId . '\'');
        $rows = $stmt->executeQuery()->fetchAllAssociative();
        return new JsonResponse(["committed" => true]);
    }
}
