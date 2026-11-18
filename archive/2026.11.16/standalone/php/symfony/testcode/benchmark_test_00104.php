<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00104', methods: ['POST'])]
class BenchmarkTest00104Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookies->get('session_token', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        if (!in_array((string)$data, ['config.json', 'index.html', 'readme.md'], true)) { return new JsonResponse(['error' => 'forbidden'], 403); }
        $checkedPath = (string)$data;
        file_put_contents((string)$checkedPath, 'data');
        return new JsonResponse(["committed" => true]);
    }
}
