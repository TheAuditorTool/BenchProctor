<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00631', methods: ['POST'])]
class BenchmarkTest00631Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT text FROM comments LIMIT 1');
        $data = ($userInput !== null) ? $userInput : '';
        $_coerced = (float)$data;
        $processed = $_coerced;
        $request->getSession()->set('data', (string) $processed);
        return new JsonResponse(["committed" => true]);
    }
}
