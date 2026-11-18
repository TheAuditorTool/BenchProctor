// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00108(req, res) {
  const userInput = req.headers.authorization || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00108 };
