// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00265(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = Buffer.from(userInput, "hex").toString();
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + data + "</section>"); return;
}

module.exports = { BenchmarkTest00265 };
