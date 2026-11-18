// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const ldapjs = require("ldapjs");
const joi = require("joi");

async function BenchmarkTest00358(req, res) {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.#%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(data);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const processed = _schemaVal;
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  ldapClient.search("ou=people,dc=example,dc=com", { filter: "(uid=" + processed + ")", scope: "sub" }, (_err, _res) => (_res ? _res.on("end", () => ldapClient.unbind()).on("error", () => ldapClient.unbind()) : ldapClient.unbind()));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00358 };
