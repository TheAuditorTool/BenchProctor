// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00561(req, res) {
  const userInput = req.headers.host || "";
  const data = `${userInput}`;
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00561 };
