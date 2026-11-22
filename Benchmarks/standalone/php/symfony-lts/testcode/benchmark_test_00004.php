<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00004', methods: ['POST'])]
class BenchmarkTest00004Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Host', '');
        $data = ($userInput !== null) ? $userInput : '';
        $_coerced = max(0, min((int)$data, 1048576));
        $boundedVal = $_coerced;
        $records = (int) $boundedVal;
        $frame = str_repeat("\0", (int) ($records * 16));
        return new JsonResponse(['frame_bytes' => strlen($frame)], 200);
    }
}
