<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00687Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->file('upload')?->getClientOriginalName() ?? '');
        $data = sprintf('%s', $userInput);
        if (!preg_match('#^(asc|desc|name|created)$#', (string)$data)) { error_log('enum validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $data;
        $ldap = ldap_connect(getenv('LDAP_URL') ?: 'ldap://directory:1389');
        ldap_set_option($ldap, LDAP_OPT_PROTOCOL_VERSION, 3);
        ldap_bind($ldap, getenv('LDAP_BIND_DN'), getenv('LDAP_BIND_PASS'));
        $entries = ldap_search($ldap, 'ou=people,dc=example,dc=com', '(uid=' . $processed . ')');
        return response()->json(['ok' => 1]);
    }
}
