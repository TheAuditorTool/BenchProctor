<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00336', methods: ['POST'])]
class BenchmarkTest00336Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $request->headers->get('Referer', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $conn->executeQuery('SELECT * FROM users WHERE id = \'' . $data . '\'');
        return new JsonResponse(["committed" => true]);
    }
}
