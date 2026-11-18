// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00313(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const data = String(userInput).replace(/\u0000/g, "");
  res.redirect(data);
}

module.exports = { BenchmarkTest00313 };
