<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00515', methods: ['POST'])]
class BenchmarkTest00515Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT bio FROM profiles LIMIT 1');
        $data = (!empty($userInput)) ? $userInput : '';
        $conn->executeQuery('SELECT * FROM users WHERE "' . str_replace('"', '""', (string)$data) . '" = 1');
        return new JsonResponse(["committed" => true]);
    }
}
