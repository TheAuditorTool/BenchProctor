// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00097(req, res) {
  const userInput = req.body?.payload || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const { parseXmlString } = require("libxmljs2");
  parseXmlString(String(data), { noent: true, dtdload: true, nonet: false });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00097 };
