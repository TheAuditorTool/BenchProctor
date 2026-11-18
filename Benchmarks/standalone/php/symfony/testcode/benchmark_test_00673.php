<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00673', methods: ['POST'])]
class BenchmarkTest00673Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT text FROM comments LIMIT 1');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $_coerced = in_array(strtolower((string)$data), ['true', '1', 'yes', 'on'], true) ? 'true' : 'false';
        $parsedBool = $_coerced;
        $request->getSession()->set('data', (string) $parsedBool);
        return new JsonResponse(["committed" => true]);
    }
}
