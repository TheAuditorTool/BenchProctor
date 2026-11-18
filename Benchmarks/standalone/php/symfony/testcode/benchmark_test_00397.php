<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00397', methods: ['POST'])]
class BenchmarkTest00397Controller
{
    public function __invoke()
    {
        $userInput = (new \Redis())->get('user_data');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        $errno = 0; $errstr = '';
        fsockopen((string)$data, 80, $errno, $errstr, 30);
        return new JsonResponse(["committed" => true]);
    }
}
