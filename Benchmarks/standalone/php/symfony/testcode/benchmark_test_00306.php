<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00306', methods: ['POST'])]
class BenchmarkTest00306Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT text FROM comments LIMIT 1');
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        $result = $conn->fetchAssociative('SELECT name FROM users WHERE id = ?', [$data]);
        if ($result === false) { return new JsonResponse(["error" => "not found"], 404); }
        $value = $result['name'];
        return new JsonResponse(["committed" => true]);
    }
}
