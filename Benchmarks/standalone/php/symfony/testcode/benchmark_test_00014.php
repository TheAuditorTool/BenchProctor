<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00014', methods: ['POST'])]
class BenchmarkTest00014Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $request->getContent();
        try { $data = json_decode($userInput, true, 512, JSON_THROW_ON_ERROR)['value'] ?? $userInput; }
        catch (\JsonException $e) { $data = $userInput; }
        $tokenBytes = random_bytes(16);
        $token = bin2hex($tokenBytes);
        $conn->executeStatement('UPDATE users SET reset_token = ? WHERE email = ?', [$token, (string)$data]);
        return new JsonResponse(['reset' => 'sent'], 200);
    }
}
