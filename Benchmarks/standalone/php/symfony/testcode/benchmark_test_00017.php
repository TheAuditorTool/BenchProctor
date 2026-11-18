<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00017', methods: ['POST'])]
class BenchmarkTest00017Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT text FROM comments LIMIT 1');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $_coerced = max(0, min((int)$data, 1048576));
        $boundedVal = $_coerced;
        $requested = (int) $boundedVal;
        $allocated = $requested + 1;
        return new JsonResponse(['allocated' => $allocated], 200);
    }
}
