// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function BenchmarkTest00194(req, res) {
  const userInput = req.body.payload || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  res.send(escapeHtml(data));
}

module.exports = { BenchmarkTest00194 };
