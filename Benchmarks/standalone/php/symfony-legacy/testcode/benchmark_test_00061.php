<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00061', methods: ['POST'])]
class BenchmarkTest00061Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT body FROM mq_messages ORDER BY id DESC LIMIT 1');
        $data = (!empty($userInput)) ? $userInput : '';
        $rows = $conn->createQueryBuilder()->select('*')->from('users')->where($conn->getDatabasePlatform()->quoteSingleIdentifier((string)$data) . ' = 1')->executeQuery()->fetchAllAssociative();
        return new JsonResponse(["committed" => true]);
    }
}
