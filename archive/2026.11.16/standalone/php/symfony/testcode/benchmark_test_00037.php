<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00037', methods: ['POST'])]
class BenchmarkTest00037Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT name FROM users LIMIT 1');
        [$data] = [$userInput, 'http'];
        simplexml_load_string($data, 'SimpleXMLElement', LIBXML_NOENT | LIBXML_DTDLOAD);
        return new JsonResponse(["committed" => true]);
    }
}
