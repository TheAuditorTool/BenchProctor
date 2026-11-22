<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00021', methods: ['POST'])]
class BenchmarkTest00021Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->files->get('upload')?->getClientOriginalName() ?? '');
        $data = (!empty($userInput)) ? $userInput : '';
        $zones = ['utc' => new \DateTimeZone('UTC'), 'berlin' => new \DateTimeZone('Europe/Berlin'), 'tokyo' => new \DateTimeZone('Asia/Tokyo')];
        $zone = $zones[(string)$data];
        $zoneName = $zone->getName();
        return new JsonResponse(["committed" => true]);
    }
}
