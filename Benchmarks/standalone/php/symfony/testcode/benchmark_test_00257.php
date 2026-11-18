<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00257', methods: ['POST'])]
class BenchmarkTest00257Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT name FROM users LIMIT 1');
        $data = "{$userInput}";
        $processed = htmlspecialchars($data, ENT_QUOTES, 'UTF-8');
        return new Response('<div>' . $processed . '</div>', 200, ['Content-Type' => 'text/html']);
    }
}
