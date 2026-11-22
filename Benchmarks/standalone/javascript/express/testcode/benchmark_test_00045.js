// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00045(req, res) {
  const userInput = req.query.id || "";
  const data = decodeURIComponent(userInput);
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + data + "</section>"); return;
}

module.exports = { BenchmarkTest00045 };
