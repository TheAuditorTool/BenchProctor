<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00124', methods: ['POST'])]
class BenchmarkTest00124Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $request->headers->get('Authorization', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $rows = $conn->createQueryBuilder()->select('*')->from('users')->where('id = :id')->setParameter('id', $data)->executeQuery()->fetchAllAssociative();
        return new JsonResponse(["committed" => true]);
    }
}
