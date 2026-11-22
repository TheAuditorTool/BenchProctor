// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00200(req, res) {
  const userInput = req.headers.referer || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const processed = data.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + processed + "</section>"); return;
}

module.exports = { BenchmarkTest00200 };
