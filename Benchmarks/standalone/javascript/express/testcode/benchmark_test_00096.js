// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00096(req, res) {
  const userInput = req.body.field || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00096 };
