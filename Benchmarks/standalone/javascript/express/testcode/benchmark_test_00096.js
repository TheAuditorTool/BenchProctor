// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00096(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const data = String(userInput).replace(/\u0000/g, "");
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  new Function("return (" + String(processed) + ");")();
  res.json({ done: true });
}

module.exports = { BenchmarkTest00096 };
