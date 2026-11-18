<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00029', methods: ['POST'])]
class BenchmarkTest00029Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Referer', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        system('gzip -f /var/app/reports/' . (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
