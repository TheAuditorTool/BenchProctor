// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00192(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const data = `${userInput}`;
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00192 };
