// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00210(req, res) {
  const userInput = req.body.payload || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00210 };
