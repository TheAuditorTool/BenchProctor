<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00453', methods: ['POST'])]
class BenchmarkTest00453Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT name FROM users LIMIT 1');
        $data = hex2bin($userInput);
        return new RedirectResponse($data);
    }
}
