<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00337', methods: ['POST'])]
class BenchmarkTest00337Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = sprintf('%s', $userInput);
        if (!preg_match('#^[a-zA-Z0-9_.\\#\\-]+$#', $data)) { error_log('input validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $data;
        $conn->executeQuery('SELECT * FROM users WHERE id = \'' . $processed . '\'');
        return new JsonResponse(["committed" => true]);
    }
}
