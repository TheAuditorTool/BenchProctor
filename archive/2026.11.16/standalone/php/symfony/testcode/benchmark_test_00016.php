<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00016', methods: ['POST'])]
class BenchmarkTest00016Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        json_decode($data, true);
        return new JsonResponse(["committed" => true]);
    }
}
