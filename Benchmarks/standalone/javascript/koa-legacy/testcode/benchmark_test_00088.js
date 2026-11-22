// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00088 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  const usersDoc = new (xmldom.DOMParser)().parseFromString(fs.readFileSync("/var/app/data/users.xml", "utf8"), "text/xml");
  xpath.evaluate("//user[name='" + data + "']", usersDoc, null, xpath.XPathResult.ANY_TYPE, null);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00088 };
