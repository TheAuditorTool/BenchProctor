// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00189(req, res) {
  const userInput = req.body || "";
  const data = userInput != null ? userInput : '';
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + data + "</section>"); return;
}

module.exports = { BenchmarkTest00189 };
