// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00446(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00446 };
