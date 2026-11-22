<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00203', methods: ['POST'])]
class BenchmarkTest00203Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $request->headers->get('X-Custom-Header', '');
        $result = $conn->fetchAssociative('SELECT name FROM users WHERE id = ?', [$userInput]);
        $value = $result['name'];
        return new JsonResponse(["committed" => true]);
    }
}
