// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00125(req, res) {
  const userInput = req.headers.referer || "";
  const data = nodeUtil.format("%s", userInput);
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  res.json({ allocated: buf.length }); return;
}

module.exports = { BenchmarkTest00125 };
