// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00135(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  new Function("return (" + String(data) + ");")();
  res.json({ done: true });
}

module.exports = { BenchmarkTest00135 };
