// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00451(req, res) {
  const userInput = req.headers.referer || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00451 };
