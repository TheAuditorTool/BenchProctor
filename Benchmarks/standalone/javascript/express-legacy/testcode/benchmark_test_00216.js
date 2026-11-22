// SPDX-License-Identifier: Apache-2.0
const ldapjs = require("ldapjs");
const zod = require("zod");

async function BenchmarkTest00216(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.#%\-]+$/).safeParse(data);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const processed = _parsed.data;
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  ldapClient.compare("uid=" + processed + ",ou=people,dc=example,dc=com", "employeeType", "manager", (_err, _matched) => ldapClient.unbind());
  res.json({ done: true });
}

module.exports = { BenchmarkTest00216 };
