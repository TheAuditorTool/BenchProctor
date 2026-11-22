// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function BenchmarkTest00237(req, res) {
  const userInput = req.headers.referer || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + escapeHtml(data) + "</section>"); return;
}

module.exports = { BenchmarkTest00237 };
