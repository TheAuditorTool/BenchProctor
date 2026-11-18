<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00663', methods: ['POST'])]
class BenchmarkTest00663Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $request->cookies->get('session_token', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $result = $conn->fetchAssociative('SELECT name FROM users WHERE id = ?', [$data]);
        $value = $result['name'];
        return new JsonResponse(["committed" => true]);
    }
}
