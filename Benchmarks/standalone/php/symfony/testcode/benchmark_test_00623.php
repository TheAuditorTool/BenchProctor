<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00623', methods: ['POST'])]
class BenchmarkTest00623Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('multipart_field', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        eval((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
