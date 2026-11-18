<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00401', methods: ['POST'])]
class BenchmarkTest00401Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = "{$userInput}";
        $digest = md5((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
