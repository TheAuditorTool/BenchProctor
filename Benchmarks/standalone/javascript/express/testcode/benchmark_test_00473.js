// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00473(req, res) {
  const userInput = req.query.id || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00473 };
