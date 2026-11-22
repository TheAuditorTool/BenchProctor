// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00178(req, res) {
  const userInput = req.cookies.session_token || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  req.app.locals.announcement = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00178 };
