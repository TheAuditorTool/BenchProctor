// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");
const zod = require("zod");

const BenchmarkTest00701 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%~\-]+$/).safeParse(data);
  if (!_parsed.success) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = _parsed.data;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + processed + "']", xmlDoc);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00701 };
