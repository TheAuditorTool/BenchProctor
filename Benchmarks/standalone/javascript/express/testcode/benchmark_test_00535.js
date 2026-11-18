// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00535(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  if (!/^[a-zA-Z0-9 _.\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  req.session.data = String(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00535 };
