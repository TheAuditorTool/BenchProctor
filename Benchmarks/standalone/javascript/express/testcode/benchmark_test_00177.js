// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00177(req, res) {
  const userInput = req.headers.authorization || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  req.app.locals.announcement = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00177 };
