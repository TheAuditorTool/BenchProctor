<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00480', methods: ['POST'])]
class BenchmarkTest00480Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Referer', '');
        $data = str_replace("\0", '', $userInput);
        $digest = hash('sha256', (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
