<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00685', methods: ['POST'])]
class BenchmarkTest00685Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Referer', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $errno = 0; $errstr = '';
        fsockopen((string)$data, 80, $errno, $errstr, 30);
        return new JsonResponse(["committed" => true]);
    }
}
