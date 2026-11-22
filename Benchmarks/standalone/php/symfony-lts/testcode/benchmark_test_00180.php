<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00180', methods: ['POST'])]
class BenchmarkTest00180Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->attributes->get('id') ?? $request->query->get('id', ''));
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        $users = simplexml_load_file('/var/app/data/users.xml');
        $matches = $users->xpath("//user[@name='" . $data . "']");
        return new JsonResponse(["committed" => true]);
    }
}
