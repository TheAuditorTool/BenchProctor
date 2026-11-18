// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00241(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00241 };
