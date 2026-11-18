<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00241', methods: ['POST'])]
class BenchmarkTest00241Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Referer', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        unlink('/var/app/data/' . $data);
        return new JsonResponse(["committed" => true]);
    }
}
