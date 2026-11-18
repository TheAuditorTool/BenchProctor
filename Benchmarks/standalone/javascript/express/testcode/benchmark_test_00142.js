// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00142(req, res) {
  const userInput = process.env.APP_INPUT || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const token = crypto.randomBytes(16).toString("hex");
  res.json({ token, label: String(data) });
}

module.exports = { BenchmarkTest00142 };
