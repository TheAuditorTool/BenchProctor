<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00250', methods: ['POST'])]
class BenchmarkTest00250Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->files->get('upload')?->getClientOriginalName() ?? '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        json_decode($data, true);
        return new JsonResponse(["committed" => true]);
    }
}
