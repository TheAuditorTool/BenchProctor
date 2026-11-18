<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00052', methods: ['POST'])]
class BenchmarkTest00052Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = ($request->attributes->get('id') ?? $request->query->get('id', ''));
        [$data] = [$userInput, 'http'];
        $conn->executeQuery('SELECT * FROM users WHERE id = \'' . $data . '\'');
        return new JsonResponse(["committed" => true]);
    }
}
