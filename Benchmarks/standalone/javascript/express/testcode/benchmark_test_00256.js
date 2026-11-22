// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00256(req, res) {
  const userInput = req.body?.payload || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00256 };
