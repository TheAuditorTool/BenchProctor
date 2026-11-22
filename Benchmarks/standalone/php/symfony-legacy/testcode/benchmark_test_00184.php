<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00184', methods: ['POST'])]
class BenchmarkTest00184Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT name FROM users LIMIT 1');
        [$data] = [$userInput, 'http'];
        $digest = sha1((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
