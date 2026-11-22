// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00325(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  new Function("return (" + String(processed) + ");")();
  res.json({ done: true });
}

module.exports = { BenchmarkTest00325 };
