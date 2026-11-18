// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function BenchmarkTest00118(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  res.send(escapeHtml(userInput));
}

module.exports = { BenchmarkTest00118 };
