<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00152', methods: ['POST'])]
class BenchmarkTest00152Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        if (!in_array((string)$data, ['config.json', 'index.html', 'readme.md'], true)) { return new JsonResponse(['error' => 'forbidden'], 403); }
        $checkedPath = (string)$data;
        file_put_contents((string)$checkedPath, 'data');
        return new JsonResponse(["committed" => true]);
    }
}
