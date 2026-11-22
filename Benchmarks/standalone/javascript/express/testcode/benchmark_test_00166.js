// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00166(req, res) {
  const userInput = req.headers.referer || "";
  const data = `${userInput}`;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + data + "</section>"); return;
}

module.exports = { BenchmarkTest00166 };
