// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function BenchmarkTest00172(req, res) {
  const userInput = req.query.id || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  http.get(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00172 };
