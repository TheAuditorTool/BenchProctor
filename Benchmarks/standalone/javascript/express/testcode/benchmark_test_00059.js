// SPDX-License-Identifier: Apache-2.0
const ldapjs = require("ldapjs");

async function BenchmarkTest00059(req, res) {
  const userInput = req.body?.variables?.input || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  const password = String(req.body?.password ?? "");
  if (!password) { res.status(400).json({ error: "password required" }); return; }
  const authenticated = await new Promise((resolve) => {
    ldapClient.bind("uid=" + processed + ",ou=people,dc=example,dc=com", password, (err) => { ldapClient.unbind(); resolve(!err); });
  });
  res.json({ authenticated }); return;
}

module.exports = { BenchmarkTest00059 };
