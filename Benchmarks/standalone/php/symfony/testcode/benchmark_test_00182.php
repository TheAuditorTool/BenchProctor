<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00182', methods: ['POST'])]
class BenchmarkTest00182Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $request->headers->get('X-Custom-Header', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $conn->executeQuery('SELECT * FROM users WHERE id = \'' . $data . '\'');
        return new JsonResponse(["committed" => true]);
    }
}
