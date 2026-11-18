// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00417(req, res) {
  const userInput = req.headers.host || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00417 };
