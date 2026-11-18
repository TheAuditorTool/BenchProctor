<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00429', methods: ['POST'])]
class BenchmarkTest00429Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->files->get('upload')?->getClientOriginalName() ?? '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $digest = hash('sha256', (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
