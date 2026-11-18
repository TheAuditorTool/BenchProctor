// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const joi = require("joi");

async function BenchmarkTest00215(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(data);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const processed = _schemaVal;
  req.session.data = String(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00215 };
