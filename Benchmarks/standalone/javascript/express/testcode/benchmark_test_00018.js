// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00018(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00018 };
