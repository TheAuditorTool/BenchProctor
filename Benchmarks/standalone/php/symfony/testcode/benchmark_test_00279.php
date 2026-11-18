<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00279', methods: ['POST'])]
class BenchmarkTest00279Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $request->request->get('field', '');
        $data = "{$userInput}";
        $conn->executeQuery('SELECT * FROM users WHERE "' . str_replace('"', '""', (string)$data) . '" = 1');
        return new JsonResponse(["committed" => true]);
    }
}
