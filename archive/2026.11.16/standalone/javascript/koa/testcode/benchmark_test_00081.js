// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");
const zod = require("zod");

const BenchmarkTest00081 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const data = nodeUtil.format("%s", userInput);
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%~\-]+$/).safeParse(data);
  if (!_parsed.success) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = _parsed.data;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + processed + "']", xmlDoc);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00081 };
