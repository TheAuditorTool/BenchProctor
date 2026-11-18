// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function BenchmarkTest00179(req, res) {
  const userInput = req.body.field || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  http.get(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00179 };
