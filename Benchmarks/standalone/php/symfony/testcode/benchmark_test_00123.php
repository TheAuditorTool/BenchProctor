<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00123', methods: ['POST'])]
class BenchmarkTest00123Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT text FROM comments LIMIT 1');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $processed = htmlspecialchars($data, ENT_QUOTES, 'UTF-8');
        return new Response('<div>' . $processed . '</div>', 200, ['Content-Type' => 'text/html']);
    }
}
