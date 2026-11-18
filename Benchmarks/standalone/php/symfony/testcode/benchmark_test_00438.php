<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00438', methods: ['POST'])]
class BenchmarkTest00438Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT text FROM comments LIMIT 1');
        $data = (!empty($userInput)) ? $userInput : '';
        $resp = new JsonResponse(['ok' => 1]);
        $resp->headers->setCookie(\Symfony\Component\HttpFoundation\Cookie::create('session', (string)$data, 0, '/', null, false, true, false, 'Strict'));
        return $resp;
    }
}
