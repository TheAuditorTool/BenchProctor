// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeUtil = require("util");
const joi = require("joi");

const BenchmarkTest00163 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = nodeUtil.format("%s", userInput);
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(data);
  if (_schemaErr) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = _schemaVal;
  ctx.app.context.announcement = String(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00163 };
