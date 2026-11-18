<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00409', methods: ['POST'])]
class BenchmarkTest00409Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT name FROM users LIMIT 1');
        $data = "{$userInput}";
        simplexml_load_string($data, 'SimpleXMLElement', LIBXML_NONET);
        return new JsonResponse(["committed" => true]);
    }
}
