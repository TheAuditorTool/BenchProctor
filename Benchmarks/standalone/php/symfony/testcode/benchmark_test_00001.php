<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00001', methods: ['POST'])]
class BenchmarkTest00001Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT body FROM mq_messages ORDER BY id DESC LIMIT 1');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        (new \Symfony\Component\Yaml\Parser())->parse($data, \Symfony\Component\Yaml\Yaml::PARSE_OBJECT | \Symfony\Component\Yaml\Yaml::PARSE_OBJECT_FOR_MAP);
        return new JsonResponse(["committed" => true]);
    }
}
