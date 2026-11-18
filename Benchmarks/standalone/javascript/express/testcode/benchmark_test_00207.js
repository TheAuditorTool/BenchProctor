// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00207(req, res) {
  const userInput = req.body.field || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  res.redirect(data);
}

module.exports = { BenchmarkTest00207 };
