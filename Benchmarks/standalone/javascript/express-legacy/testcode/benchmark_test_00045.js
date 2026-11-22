// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00045(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const processed = data.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + processed + "</section>"); return;
}

module.exports = { BenchmarkTest00045 };
