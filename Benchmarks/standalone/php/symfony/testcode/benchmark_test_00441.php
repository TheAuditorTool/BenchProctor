<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;
use Doctrine\ORM\EntityManagerInterface;

#[Route('/BenchmarkTest00441', methods: ['POST'])]
class BenchmarkTest00441Controller
{
    public function __invoke(Connection $conn, EntityManagerInterface $em)
    {
        $userInput = $conn->fetchOne('SELECT body FROM mq_messages ORDER BY id DESC LIMIT 1');
        $data = sprintf('%s', $userInput);
        $em->getRepository(\App\Entity\User::class)->find((int)$data);
        return new JsonResponse(["committed" => true]);
    }
}
