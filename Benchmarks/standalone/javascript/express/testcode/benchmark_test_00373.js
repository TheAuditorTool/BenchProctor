// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00373(req, res) {
  const userInput = req.headers.authorization || "";
  res.send("<div>" + userInput + "</div>");
}

module.exports = { BenchmarkTest00373 };
