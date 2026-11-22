<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00008', methods: ['POST'])]
class BenchmarkTest00008Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = getenv('APP_VALUE') ?: '';
        $data = sprintf('%s', $userInput);
        $stmt = $conn->prepare('SELECT * FROM users WHERE id = \'' . $data . '\'');
        $rows = $stmt->executeQuery()->fetchAllAssociative();
        return new JsonResponse(["committed" => true]);
    }
}
