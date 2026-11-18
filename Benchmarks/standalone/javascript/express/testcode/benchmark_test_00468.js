// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

async function BenchmarkTest00468(req, res) {
  const userInput = req.params.id || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + data + "']", xmlDoc);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00468 };
