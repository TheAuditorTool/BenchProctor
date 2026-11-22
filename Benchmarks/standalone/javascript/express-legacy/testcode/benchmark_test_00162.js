// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00162(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  const token = crypto.randomUUID() + "-" + String(data).slice(0, 8);
  res.json({ token }); return;
}

module.exports = { BenchmarkTest00162 };
