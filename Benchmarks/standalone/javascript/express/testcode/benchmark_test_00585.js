// SPDX-License-Identifier: Apache-2.0
const zod = require("zod");

async function BenchmarkTest00585(req, res) {
  const userInput = req.body.multipart_field || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.\-]+$/).safeParse(data);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const processed = _parsed.data;
  req.session.data = String(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00585 };
