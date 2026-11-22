// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function BenchmarkTest00066(req, res) {
  const userInput = req.cookies.session_token || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  http.get(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00066 };
