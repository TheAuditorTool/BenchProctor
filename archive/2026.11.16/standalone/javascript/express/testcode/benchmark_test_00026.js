// SPDX-License-Identifier: Apache-2.0
const zod = require("zod");

async function BenchmarkTest00026(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const data = String(userInput).slice(0, 200);
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.\-]+$/).safeParse(data);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const processed = _parsed.data;
  req.session.data = String(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00026 };
