// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00199(req, res) {
  const userInput = req.body?.variables?.input || "";
  const data = String(userInput).replace(/\u0000/g, "");
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  req.app.locals.announcement = String(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00199 };
