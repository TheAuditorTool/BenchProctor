<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00106', methods: ['POST'])]
class BenchmarkTest00106Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Forwarded-For', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $digest = md5((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
