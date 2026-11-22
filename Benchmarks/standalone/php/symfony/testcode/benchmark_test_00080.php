<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00080', methods: ['POST'])]
class BenchmarkTest00080Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $data = sprintf('%s', $userInput);
        $rows = $conn->createQueryBuilder()->select('*')->from('users')->where('id = :id')->setParameter('id', $data)->executeQuery()->fetchAllAssociative();
        return new JsonResponse(["committed" => true]);
    }
}
