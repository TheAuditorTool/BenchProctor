<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00517', methods: ['POST'])]
class BenchmarkTest00517Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Host', '');
        $data = sprintf('%s', $userInput);
        $requested = (int) $data;
        $wrapped = unpack('l', pack('l', $requested + 1))[1];
        return new JsonResponse(['wrapped' => $wrapped], 200);
    }
}
