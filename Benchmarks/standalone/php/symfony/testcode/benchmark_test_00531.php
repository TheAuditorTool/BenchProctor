<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00531', methods: ['POST'])]
class BenchmarkTest00531Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $request->query->get('id', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        if (!preg_match('#^(asc|desc|name|created)$#', (string)$data)) { error_log('enum validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $data;
        $conn->executeQuery('SELECT * FROM users ORDER BY ' . $processed);
        return new JsonResponse(["committed" => true]);
    }
}
