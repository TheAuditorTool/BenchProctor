<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00126', methods: ['POST'])]
class BenchmarkTest00126Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('multipart_field', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $content = file_get_contents('/var/app/data/' . (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
