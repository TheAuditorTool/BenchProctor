// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const joi = require("joi");

const BenchmarkTest00085 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(data);
  if (_schemaErr) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = _schemaVal;
  ctx.session.data = String(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00085 };
