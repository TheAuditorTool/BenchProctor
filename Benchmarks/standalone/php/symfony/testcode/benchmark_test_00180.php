<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00180', methods: ['POST'])]
class BenchmarkTest00180Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = (new \Redis())->get('user_data');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $rows = $conn->createQueryBuilder()->select('*')->from('users')->where('id = \'' . $data . '\'')->executeQuery()->fetchAllAssociative();
        return new JsonResponse(["committed" => true]);
    }
}
