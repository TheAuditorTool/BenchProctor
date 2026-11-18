// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00132 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const _coerced = Math.max(0, Math.min(parseInt(String(data), 10) || 0, 1048576));
  const boundedVal = _coerced;
  const requested = boundedVal;
  if (!Number.isFinite(requested) || requested < 0 || requested > 1048576) { ctx.status = 400; ctx.body = { error: "out of range" }; return; }
  const buf = Buffer.alloc(requested + 1);
  ctx.body = { allocated: buf.length }; return;
}

module.exports = { BenchmarkTest00132 };
