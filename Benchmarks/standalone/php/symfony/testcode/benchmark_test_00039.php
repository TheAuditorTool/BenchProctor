<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00039', methods: ['POST'])]
class BenchmarkTest00039Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Custom-Header', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        system('gzip -f /var/app/reports/' . (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
