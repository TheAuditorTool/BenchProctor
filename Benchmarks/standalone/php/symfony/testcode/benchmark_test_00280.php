<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00280', methods: ['POST'])]
class BenchmarkTest00280Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->files->get('upload')?->getClientOriginalName() ?? '');
        $data = ($userInput !== null) ? $userInput : '';
        json_decode($data, true);
        return new JsonResponse(["committed" => true]);
    }
}
