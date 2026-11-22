// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00234(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00234 };
