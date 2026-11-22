// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const ldapjs = require("ldapjs");
const joi = require("joi");

async function BenchmarkTest00342(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.#%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(data);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const processed = _schemaVal;
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  const password = String(req.body.password ?? "");
  if (!password) { res.status(400).json({ error: "password required" }); return; }
  const authenticated = await new Promise((resolve) => {
    ldapClient.bind("uid=" + processed + ",ou=people,dc=example,dc=com", password, (err) => { ldapClient.unbind(); resolve(!err); });
  });
  res.json({ authenticated }); return;
}

module.exports = { BenchmarkTest00342 };
