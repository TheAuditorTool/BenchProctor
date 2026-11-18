<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00718', methods: ['POST'])]
class BenchmarkTest00718Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = (!empty($userInput)) ? $userInput : '';
        $result = $conn->fetchAssociative('SELECT name FROM users WHERE id = ?', [$data]);
        if ($result === false) { return new JsonResponse(["error" => "not found"], 404); }
        $value = $result['name'];
        return new JsonResponse(["committed" => true]);
    }
}
