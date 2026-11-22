// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");
const joi = require("joi");

const BenchmarkTest00072 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  const data = nodeUtil.format("%s", userInput);
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%~\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(data);
  if (_schemaErr) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = _schemaVal;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + processed + "']", xmlDoc);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00072 };
