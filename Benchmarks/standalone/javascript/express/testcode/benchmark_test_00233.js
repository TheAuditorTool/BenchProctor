// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00233(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00233 };
