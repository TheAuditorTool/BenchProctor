// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00071(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00071 };
