// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00256(req, res) {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  await db.query("SELECT * FROM users ORDER BY " + processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00256 };
