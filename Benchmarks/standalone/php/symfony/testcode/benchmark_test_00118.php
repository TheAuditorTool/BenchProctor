<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00118', methods: ['POST'])]
class BenchmarkTest00118Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Authorization', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $zones = ['utc' => new \DateTimeZone('UTC'), 'berlin' => new \DateTimeZone('Europe/Berlin'), 'tokyo' => new \DateTimeZone('Asia/Tokyo')];
        $zone = $zones[(string)$data] ?? null;
        if ($zone === null) { return new JsonResponse(["error" => "not found"], 404); }
        $zoneName = $zone->getName();
        return new JsonResponse(["committed" => true]);
    }
}
