// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");
const joi = require("joi");

async function BenchmarkTest00346(req, res) {
  const userInput = req.headers.origin || "";
  const data = nodeUtil.format("%s", userInput);
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%~\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(data);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const processed = _schemaVal;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + processed + "']", xmlDoc);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00346 };
