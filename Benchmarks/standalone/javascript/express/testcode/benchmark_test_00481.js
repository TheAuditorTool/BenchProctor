// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00481(req, res) {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const _coerced = Math.max(0, Math.min(parseInt(String(data), 10) || 0, 1048576));
  const boundedVal = _coerced;
  const requested = boundedVal;
  if (!Number.isFinite(requested) || requested < 0 || requested > 1048576) { res.status(400).json({ error: "out of range" }); return; }
  const buf = Buffer.alloc(requested + 1);
  res.json({ allocated: buf.length }); return;
}

module.exports = { BenchmarkTest00481 };
