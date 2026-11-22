<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00140', methods: ['POST'])]
class BenchmarkTest00140Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = file_get_contents('http://api.corp.lan/data');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $rows = $conn->createQueryBuilder()->select('*')->from('users')->where('id = \'' . $data . '\'')->executeQuery()->fetchAllAssociative();
        return new JsonResponse(["committed" => true]);
    }
}
