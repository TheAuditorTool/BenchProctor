// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00560(req, res) {
  const userInput = req.body || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00560 };
