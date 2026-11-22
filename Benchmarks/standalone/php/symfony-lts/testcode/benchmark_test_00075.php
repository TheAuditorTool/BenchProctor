<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00075', methods: ['POST'])]
class BenchmarkTest00075Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('multipart_field', '');
        $checkedPath = '/var/app/data/' . basename($userInput);
        $content = file_get_contents($checkedPath);
        return new JsonResponse(["committed" => true]);
    }
}
