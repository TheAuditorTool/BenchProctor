// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00401(req, res) {
  const userInput = req.body.payload || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  eval(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00401 };
