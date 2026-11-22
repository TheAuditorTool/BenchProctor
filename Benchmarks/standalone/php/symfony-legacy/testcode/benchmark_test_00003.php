<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00003', methods: ['POST'])]
class BenchmarkTest00003Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT text FROM comments LIMIT 1');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $rows = $conn->createQueryBuilder()->select('*')->from('users')->where('id = \'' . $data . '\'')->executeQuery()->fetchAllAssociative();
        return new JsonResponse(["committed" => true]);
    }
}
