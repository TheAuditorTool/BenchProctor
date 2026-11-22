// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00054(req, res) {
  const userInput = req.body.multipart_field || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  res.redirect(data);
}

module.exports = { BenchmarkTest00054 };
