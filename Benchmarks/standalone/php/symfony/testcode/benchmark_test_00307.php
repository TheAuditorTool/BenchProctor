<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00307', methods: ['POST'])]
class BenchmarkTest00307Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        if (!in_array((string)$userInput, ['config.json', 'index.html', 'readme.md'], true)) { return new JsonResponse(['error' => 'forbidden'], 403); }
        $checkedPath = (string)$userInput;
        file_put_contents((string)$checkedPath, 'data');
        return new JsonResponse(["committed" => true]);
    }
}
