<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00247', methods: ['POST'])]
class BenchmarkTest00247Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT text FROM comments LIMIT 1');
        $data = (!empty($userInput)) ? $userInput : '';
        $digest = md5((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
