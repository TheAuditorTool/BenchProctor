<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00124', methods: ['POST'])]
class BenchmarkTest00124Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = file_get_contents('/tmp/data');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        if (!preg_match('#^[a-zA-Z0-9_.\\#\\-]+$#', $data)) { error_log('input validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $data;
        $rows = $conn->createQueryBuilder()->select('*')->from('users')->where('id = \'' . $processed . '\'')->executeQuery()->fetchAllAssociative();
        return new JsonResponse(["committed" => true]);
    }
}
