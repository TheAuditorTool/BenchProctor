<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00137', methods: ['POST'])]
class BenchmarkTest00137Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = file_get_contents('http://api.corp.lan/data');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $rows = $conn->createQueryBuilder()->select('*')->from('users')->where('id = :id')->setParameter('id', $data)->executeQuery()->fetchAllAssociative();
        return new JsonResponse(["committed" => true]);
    }
}
