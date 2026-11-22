// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00120(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00120 };
