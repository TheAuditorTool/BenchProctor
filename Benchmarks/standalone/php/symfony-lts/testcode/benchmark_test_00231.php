<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00231', methods: ['POST'])]
class BenchmarkTest00231Controller
{
    public function __invoke()
    {
        $userInput = (new \Redis())->get('user_data');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        unserialize($data);
        return new JsonResponse(["committed" => true]);
    }
}
