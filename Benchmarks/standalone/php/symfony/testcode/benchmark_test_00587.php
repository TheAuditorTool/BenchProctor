<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00587', methods: ['POST'])]
class BenchmarkTest00587Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = file_get_contents('http://api.corp.lan/data');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $conn->executeQuery('SELECT * FROM users WHERE id = \'' . $data . '\'');
        return new JsonResponse(["committed" => true]);
    }
}
