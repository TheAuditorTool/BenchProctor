// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00007(req, res) {
  const userInput = req.params.id || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00007 };
