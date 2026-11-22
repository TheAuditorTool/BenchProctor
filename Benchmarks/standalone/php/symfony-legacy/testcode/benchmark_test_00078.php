<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00078', methods: ['POST'])]
class BenchmarkTest00078Controller
{
    public function __invoke(Request $request, Connection $conn)
    {
        $userInput = $request->headers->get('User-Agent', '');
        try { $data = json_decode($userInput, true, 512, JSON_THROW_ON_ERROR)['value'] ?? $userInput; }
        catch (\JsonException $e) { $data = $userInput; }
        $alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
        $shuffled = str_shuffle(str_repeat($alphabet, 4));
        $token = substr($shuffled, 0, 32);
        $conn->executeStatement('UPDATE users SET reset_token = ? WHERE email = ?', [$token, (string)$data]);
        return new JsonResponse(['reset' => 'sent'], 200);
    }
}
