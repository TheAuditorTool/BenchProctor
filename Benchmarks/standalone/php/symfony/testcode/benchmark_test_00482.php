<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00482', methods: ['POST'])]
class BenchmarkTest00482Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $data = vsprintf('%1$s', [$userInput]);
        $result = $conn->fetchAssociative('SELECT name FROM users WHERE id = ?', [$data]);
        $value = $result['name'];
        return new JsonResponse(["committed" => true]);
    }
}
