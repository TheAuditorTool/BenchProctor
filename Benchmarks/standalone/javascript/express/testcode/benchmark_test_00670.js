// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const zod = require("zod");

async function BenchmarkTest00670(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = `${userInput}`;
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.\-]+$/).safeParse(data);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const processed = _parsed.data;
  req.session.data = String(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00670 };
