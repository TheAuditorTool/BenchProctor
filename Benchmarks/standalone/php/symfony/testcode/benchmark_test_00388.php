<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00388', methods: ['POST'])]
class BenchmarkTest00388Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = ($request->attributes->get('id') ?? $request->query->get('id', ''));
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $result = $conn->fetchAssociative('SELECT name FROM users WHERE id = ?', [$data]);
        if ($result === false) { return new JsonResponse(["error" => "not found"], 404); }
        $value = $result['name'];
        return new JsonResponse(["committed" => true]);
    }
}
