// SPDX-License-Identifier: Apache-2.0

async function annotateLedger(req, res) {
  const phrase = req.headers.authorization || "";
  const inquiry = Buffer.from(phrase, "base64").toString();
  res.send("<div>" + inquiry + "</div>");
}

module.exports = { annotateLedger };
