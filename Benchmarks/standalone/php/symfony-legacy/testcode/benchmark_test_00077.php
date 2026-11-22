<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00077', methods: ['POST'])]
class BenchmarkTest00077Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $request->cookies->get('session_token', '');
        $data = str_replace("\0", '', $userInput);
        $_coerced = (int)$data;
        $parsedId = $_coerced;
        $rows = $conn->createQueryBuilder()->select('*')->from('users')->where('id = \'' . $parsedId . '\'')->executeQuery()->fetchAllAssociative();
        return new JsonResponse(["committed" => true]);
    }
}
