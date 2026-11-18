// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00041(req, res) {
  const userInput = req.headers.referer || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  res.redirect(data);
}

module.exports = { BenchmarkTest00041 };
