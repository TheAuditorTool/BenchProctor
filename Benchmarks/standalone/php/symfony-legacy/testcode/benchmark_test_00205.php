<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00205', methods: ['POST'])]
class BenchmarkTest00205Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = ($request->attributes->get('id') ?? $request->query->get('id', ''));
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $token = (string) (int) (lcg_value() * 1000000000000);
        $conn->executeStatement('UPDATE users SET reset_token = ? WHERE email = ?', [$token, (string)$data]);
        return new JsonResponse(['reset' => 'sent'], 200);
    }
}
