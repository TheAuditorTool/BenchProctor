<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00148', methods: ['POST'])]
class BenchmarkTest00148Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookies->get('session_token', '');
        $data = "{$userInput}";
        $records = (int) $data;
        $frame = str_repeat("\0", (int) ($records * 16));
        return new JsonResponse(['frame_bytes' => strlen($frame)], 200);
    }
}
