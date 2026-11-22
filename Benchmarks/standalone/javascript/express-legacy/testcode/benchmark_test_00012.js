// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00012(req, res) {
  const userInput = req.headers.referer || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  new Function("return (" + String(processed) + ");")();
  res.json({ done: true });
}

module.exports = { BenchmarkTest00012 };
