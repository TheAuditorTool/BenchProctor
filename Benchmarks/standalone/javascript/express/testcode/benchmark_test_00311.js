// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00311(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00311 };
