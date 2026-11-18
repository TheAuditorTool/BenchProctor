// SPDX-License-Identifier: Apache-2.0
const zod = require("zod");

async function BenchmarkTest00423(req, res) {
  const userInput = req.headers.host || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.\-]+$/).safeParse(data);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const processed = _parsed.data;
  req.session.data = String(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00423 };
