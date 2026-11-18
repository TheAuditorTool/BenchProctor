<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00072', methods: ['POST'])]
class BenchmarkTest00072Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Custom-Header', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        system('gzip -f /var/app/reports/' . (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
