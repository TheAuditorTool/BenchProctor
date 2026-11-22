// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00347(req, res) {
  const userInput = req.headers.host || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00347 };
