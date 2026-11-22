<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00015', methods: ['POST'])]
class BenchmarkTest00015Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT name FROM users LIMIT 1');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $doc = new \DOMDocument();
        $doc->loadXML((string)$data, LIBXML_NONET);
        $name = $doc->getElementsByTagName('name')->item(0)?->textContent;
        return new JsonResponse(["committed" => true]);
    }
}
