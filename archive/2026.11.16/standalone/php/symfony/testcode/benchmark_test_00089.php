<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;
use Doctrine\ORM\EntityManagerInterface;

#[Route('/BenchmarkTest00089', methods: ['POST'])]
class BenchmarkTest00089Controller
{
    public function __invoke(Connection $conn, EntityManagerInterface $em)
    {
        $userInput = $conn->fetchOne('SELECT text FROM comments LIMIT 1');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $em->getRepository(\App\Entity\User::class)->find((int)$data);
        return new JsonResponse(["committed" => true]);
    }
}
