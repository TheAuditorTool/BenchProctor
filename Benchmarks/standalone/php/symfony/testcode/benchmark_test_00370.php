<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00370', methods: ['POST'])]
class BenchmarkTest00370Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        if (!in_array((string)$data, ['ls', 'cat', 'date', 'whoami'], true)) { return new JsonResponse(['error' => 'forbidden'], 403); }
        $allowedBin = (string)$data;
        system('gzip -f /var/app/reports/' . (string)$allowedBin);
        return new JsonResponse(["committed" => true]);
    }
}
