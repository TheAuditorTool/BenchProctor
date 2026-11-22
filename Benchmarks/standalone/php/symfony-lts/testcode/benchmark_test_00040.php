<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00040', methods: ['POST'])]
class BenchmarkTest00040Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Referer', '');
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        $records = (int) $data;
        $frame = str_repeat("\0", (int) ($records * 16));
        return new JsonResponse(['frame_bytes' => strlen($frame)], 200);
    }
}
