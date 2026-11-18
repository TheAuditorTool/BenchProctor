<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\Validator\Validation;
use Symfony\Component\Validator\Constraints as Assert;

#[Route('/BenchmarkTest00349', methods: ['POST'])]
class BenchmarkTest00349Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['variables']['input'] ?? '';
        $pending = explode(',', $userInput);
        $data = '';
        while (count($pending)) { $data = array_shift($pending); }
        $_violations = Validation::createValidator()->validate((string)$data, [new Assert\Regex(['pattern' => '#^[a-zA-Z0-9 _.\\#%\\-]+$#'])]);
        if (count($_violations) > 0) { error_log('schema validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = (string)$data;
        $ldap = ldap_connect(getenv('LDAP_URL') ?: 'ldap://directory:1389');
        ldap_set_option($ldap, LDAP_OPT_PROTOCOL_VERSION, 3);
        ldap_bind($ldap, getenv('LDAP_BIND_DN'), getenv('LDAP_BIND_PASS'));
        $entries = ldap_search($ldap, 'ou=people,dc=example,dc=com', '(uid=' . $processed . ')');
        return new JsonResponse(["committed" => true]);
    }
}
