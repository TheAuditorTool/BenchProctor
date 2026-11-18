<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00103', methods: ['POST'])]
class BenchmarkTest00103Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->files->get('upload')?->getClientOriginalName() ?? '');
        $pending = explode(',', $userInput);
        $data = '';
        while (count($pending)) { $data = array_shift($pending); }
        $resolved = realpath('/var/app/data/' . $data);
        if ($resolved === false || strpos($resolved, '/var/app/data/') !== 0) { return new JsonResponse(['error'=>'forbidden'], 403); }
        $checkedPath = $resolved;
        $content = file_get_contents($checkedPath);
        return new JsonResponse(["committed" => true]);
    }
}
