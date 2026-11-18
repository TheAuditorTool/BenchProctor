<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00156', methods: ['POST'])]
class BenchmarkTest00156Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->files->get('upload')?->getClientOriginalName() ?? '');
        try { $data = json_decode($userInput, true, 512, JSON_THROW_ON_ERROR)['value'] ?? $userInput; }
        catch (\JsonException $e) { $data = $userInput; }
        $digest = hash('sha256', (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
