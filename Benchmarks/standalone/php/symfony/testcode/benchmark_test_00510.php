<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00510', methods: ['POST'])]
class BenchmarkTest00510Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT bio FROM profiles LIMIT 1');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        file_put_contents('/var/uploads/' . $data, 'data');
        return new JsonResponse(["committed" => true]);
    }
}
