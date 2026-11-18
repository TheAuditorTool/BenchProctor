// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");
const zod = require("zod");

async function BenchmarkTest00003(req, res) {
  const userInput = req.body.multipart_field || "";
  const data = nodeUtil.format("%s", userInput);
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%~\-]+$/).safeParse(data);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const processed = _parsed.data;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + processed + "']", xmlDoc);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00003 };
