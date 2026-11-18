<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00644', methods: ['POST'])]
class BenchmarkTest00644Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT body FROM mq_messages ORDER BY id DESC LIMIT 1');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        json_decode($data, true);
        return new JsonResponse(["committed" => true]);
    }
}
