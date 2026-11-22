<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00143', methods: ['POST'])]
class BenchmarkTest00143Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = file_get_contents('/tmp/data');
        $data = hex2bin($userInput);
        $_coerced = (int)$data;
        $parsedId = $_coerced;
        $stmt = $conn->prepare('SELECT * FROM users WHERE id = \'' . $parsedId . '\'');
        $rows = $stmt->executeQuery()->fetchAllAssociative();
        return new JsonResponse(["committed" => true]);
    }
}
