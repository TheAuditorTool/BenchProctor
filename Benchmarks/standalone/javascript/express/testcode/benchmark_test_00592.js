// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00592(req, res) {
  const userInput = req.body || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00592 };
