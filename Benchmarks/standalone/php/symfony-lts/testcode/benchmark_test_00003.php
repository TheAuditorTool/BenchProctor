<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00003', methods: ['POST'])]
class BenchmarkTest00003Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = (new \Redis())->get('user_data');
        $data = (!empty($userInput)) ? $userInput : '';
        $_coerced = (int)$data;
        $parsedId = $_coerced;
        $stmt = $conn->prepare('SELECT * FROM users WHERE id = \'' . $parsedId . '\'');
        $rows = $stmt->executeQuery()->fetchAllAssociative();
        return new JsonResponse(["committed" => true]);
    }
}
