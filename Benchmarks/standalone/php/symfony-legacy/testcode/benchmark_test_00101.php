<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\Routing\Annotation\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00101', methods: ['POST'])]
class BenchmarkTest00101Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT name FROM users LIMIT 1');
        $data = hex2bin($userInput);
        $stream = function () use ($data) {
            echo '<div class="comment">' . $data . '</div>';
        };
        return new \Symfony\Component\HttpFoundation\StreamedResponse($stream, 200, ['Content-Type' => 'text/html']);
    }
}
