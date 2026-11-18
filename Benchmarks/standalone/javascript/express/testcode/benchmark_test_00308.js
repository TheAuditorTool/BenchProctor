// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00308(req, res) {
  const userInput = req.query.id || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00308 };
