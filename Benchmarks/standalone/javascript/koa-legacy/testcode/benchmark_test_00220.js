// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const ldapjs = require("ldapjs");
const joi = require("joi");

const BenchmarkTest00220 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = nodeUtil.format("%s", userInput);
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.#%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(data);
  if (_schemaErr) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = _schemaVal;
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  ldapClient.compare("uid=" + processed + ",ou=people,dc=example,dc=com", "employeeType", "manager", (_err, _matched) => ldapClient.unbind());
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00220 };
