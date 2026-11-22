<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00053', methods: ['POST'])]
class BenchmarkTest00053Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $request->request->get('multipart_field', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
        $token = '';
        for ($i = 0; $i < 32; $i++) {
            $token .= $alphabet[random_int(0, strlen($alphabet) - 1)];
        }
        $conn->executeStatement('UPDATE users SET reset_token = ? WHERE email = ?', [$token, (string)$data]);
        return new JsonResponse(['reset' => 'sent'], 200);
    }
}
