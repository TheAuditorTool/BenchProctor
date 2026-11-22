// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00034(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = userInput != null ? userInput : '';
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + data + "</section>"); return;
}

module.exports = { BenchmarkTest00034 };
