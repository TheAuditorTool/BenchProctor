// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00097(req, res) {
  const userInput = req.cookies.session_token || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  res.redirect(data);
}

module.exports = { BenchmarkTest00097 };
