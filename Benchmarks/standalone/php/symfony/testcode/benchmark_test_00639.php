<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00639', methods: ['POST'])]
class BenchmarkTest00639Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        [$data] = [$userInput, 'http'];
        $requested = (int) $data;
        $wrapped = unpack('l', pack('l', $requested + 1))[1];
        return new JsonResponse(['wrapped' => $wrapped], 200);
    }
}
