<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00702', methods: ['POST'])]
class BenchmarkTest00702Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT bio FROM profiles LIMIT 1');
        if (!preg_match('#^[a-zA-Z0-9 _.\\#~\\-]+$#', $userInput)) { error_log('input validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $userInput;
        $content = file_get_contents('/var/app/data/' . (string)$processed);
        return new JsonResponse(["committed" => true]);
    }
}
