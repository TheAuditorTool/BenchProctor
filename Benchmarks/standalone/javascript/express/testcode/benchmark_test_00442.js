// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00442(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const data = `${userInput}`;
  res.redirect(data);
}

module.exports = { BenchmarkTest00442 };
