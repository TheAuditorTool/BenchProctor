<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00089', methods: ['POST'])]
class BenchmarkTest00089Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = (new \Redis())->get('user_data');
        $data = str_replace("\0", '', $userInput);
        $conn->executeQuery('SELECT * FROM users WHERE id = \'' . $data . '\'');
        return new JsonResponse(["committed" => true]);
    }
}
