<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00408', methods: ['POST'])]
class BenchmarkTest00408Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $request->query->get('id', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        if (!preg_match('#^[a-zA-Z0-9_.\\#\\-]+$#', $data)) { error_log('input validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $data;
        $conn->executeQuery('SELECT * FROM users WHERE id = \'' . $processed . '\'');
        return new JsonResponse(["committed" => true]);
    }
}
