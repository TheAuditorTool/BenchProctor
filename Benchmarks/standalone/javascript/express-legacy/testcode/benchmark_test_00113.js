// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

async function BenchmarkTest00113(req, res) {
  const userInput = req.body.field || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  await libxmljs.parseXmlAsync(String(data), { replaceEntities: false });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00113 };
