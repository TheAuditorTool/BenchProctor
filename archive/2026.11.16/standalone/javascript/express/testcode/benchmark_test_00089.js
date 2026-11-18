// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00089(req, res) {
  const userInput = (await (await fetch("https://api.partner.example/v1/records")).json()).data || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  res.redirect(data);
}

module.exports = { BenchmarkTest00089 };
