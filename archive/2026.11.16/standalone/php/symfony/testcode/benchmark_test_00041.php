<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00041', methods: ['POST'])]
class BenchmarkTest00041Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookies->get('session_token', '');
        $data = vsprintf('%1$s', [$userInput]);
        $requested = (int) $data;
        $wrapped = unpack('l', pack('l', $requested + 1))[1];
        return new JsonResponse(['wrapped' => $wrapped], 200);
    }
}
