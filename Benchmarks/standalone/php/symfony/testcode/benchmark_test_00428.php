<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00428', methods: ['POST'])]
class BenchmarkTest00428Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = getenv('APP_VALUE') ?: '';
        $data = (!empty($userInput)) ? $userInput : '';
        $conn->executeQuery('SELECT * FROM users WHERE id = \'' . $data . '\'');
        return new JsonResponse(["committed" => true]);
    }
}
