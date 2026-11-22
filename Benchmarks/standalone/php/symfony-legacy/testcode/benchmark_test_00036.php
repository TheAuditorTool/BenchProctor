<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00036', methods: ['POST'])]
class BenchmarkTest00036Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT name FROM users LIMIT 1');
        $data = vsprintf('%1$s', [$userInput]);
        $_coerced = in_array(strtolower((string)$data), ['true', '1', 'yes', 'on'], true) ? 'true' : 'false';
        $parsedBool = $_coerced;
        $compiled = tempnam('/var/app/cache', 'rule_');
        file_put_contents($compiled, '<?php return static fn (array $order) => ' . $parsedBool . ';');
        $rule = include $compiled;
        unlink($compiled);
        $result = $rule(['total' => 100, 'items' => 3]);
        return new JsonResponse(["committed" => true]);
    }
}
