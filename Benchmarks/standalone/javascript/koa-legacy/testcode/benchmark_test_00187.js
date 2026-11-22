// SPDX-License-Identifier: Apache-2.0
const ldapjs = require("ldapjs");
const zod = require("zod");

const BenchmarkTest00187 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.#%\-]+$/).safeParse(data);
  if (!_parsed.success) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = _parsed.data;
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  ldapClient.compare("uid=" + processed + ",ou=people,dc=example,dc=com", "employeeType", "manager", (_err, _matched) => ldapClient.unbind());
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00187 };
