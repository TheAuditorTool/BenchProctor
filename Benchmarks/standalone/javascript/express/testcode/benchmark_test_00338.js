// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00338(req, res) {
  const userInput = req.body?.multipart_field || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  return res.status(302).set("Location", String(data)).end();
}

module.exports = { BenchmarkTest00338 };
