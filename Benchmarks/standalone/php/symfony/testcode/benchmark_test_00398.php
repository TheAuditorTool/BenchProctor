<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00398', methods: ['POST'])]
class BenchmarkTest00398Controller
{
    public function __invoke()
    {
        $userInput = (new \Redis())->get('user_data');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        json_decode($data, true);
        return new JsonResponse(["committed" => true]);
    }
}
