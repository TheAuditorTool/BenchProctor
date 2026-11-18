<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00074', methods: ['POST'])]
class BenchmarkTest00074Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->files->get('upload')?->getClientOriginalName() ?? '');
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        unlink('/var/app/data/' . $data);
        return new JsonResponse(["committed" => true]);
    }
}
