<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00130', methods: ['POST'])]
class BenchmarkTest00130Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookies->get('session_token', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        file_put_contents('/var/uploads/' . $data, 'data');
        return new JsonResponse(["committed" => true]);
    }
}
