<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00010', methods: ['POST'])]
class BenchmarkTest00010Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $request->headers->get('Origin', '');
        $pending = explode(',', $userInput);
        $data = '';
        while (count($pending)) { $data = array_shift($pending); }
        $result = $conn->fetchAssociative('SELECT name FROM users WHERE id = ?', [$data]);
        $value = $result['name'];
        return new JsonResponse(["committed" => true]);
    }
}
