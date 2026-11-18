// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00350(req, res) {
  const userInput = req.headers.referer || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00350 };
