<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00089', methods: ['POST'])]
class BenchmarkTest00089Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Authorization', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        unserialize($data);
        return new JsonResponse(["committed" => true]);
    }
}
