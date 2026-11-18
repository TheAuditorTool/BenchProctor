// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function BenchmarkTest00607(req, res) {
  const userInput = req.query.id || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  net.connect(80, new URL(String(data)).hostname);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00607 };
