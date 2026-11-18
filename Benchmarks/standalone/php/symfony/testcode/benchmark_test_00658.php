<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00658', methods: ['POST'])]
class BenchmarkTest00658Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = ($request->attributes->get('id') ?? $request->query->get('id', ''));
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $result = $conn->fetchAssociative('SELECT name FROM users WHERE id = ?', [$data]);
        $value = $result['name'];
        return new JsonResponse(["committed" => true]);
    }
}
