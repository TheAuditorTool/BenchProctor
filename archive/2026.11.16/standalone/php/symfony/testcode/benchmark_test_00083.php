<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00083', methods: ['POST'])]
class BenchmarkTest00083Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $request->headers->get('X-Forwarded-For', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        $result = $conn->fetchAssociative('SELECT name FROM users WHERE id = ?', [$data]);
        $value = $result['name'];
        return new JsonResponse(["committed" => true]);
    }
}
