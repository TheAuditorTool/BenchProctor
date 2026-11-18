// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00022(req, res) {
  const userInput = req.headers.host || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00022 };
