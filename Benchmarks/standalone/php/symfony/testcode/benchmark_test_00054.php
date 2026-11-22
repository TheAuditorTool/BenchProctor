<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00054', methods: ['POST'])]
class BenchmarkTest00054Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $requested = (int) $data;
        $wrapped = unpack('l', pack('l', $requested + 1))[1];
        return new JsonResponse(['wrapped' => $wrapped], 200);
    }
}
