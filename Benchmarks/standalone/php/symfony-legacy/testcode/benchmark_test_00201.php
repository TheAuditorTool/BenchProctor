<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00201', methods: ['POST'])]
class BenchmarkTest00201Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = getenv('APP_VALUE') ?: '';
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $stmt = $conn->prepare('SELECT * FROM users WHERE id = \'' . $data . '\'');
        $rows = $stmt->executeQuery()->fetchAllAssociative();
        return new JsonResponse(["committed" => true]);
    }
}
