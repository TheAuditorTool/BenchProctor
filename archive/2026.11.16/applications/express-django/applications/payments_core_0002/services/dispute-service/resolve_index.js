// SPDX-License-Identifier: Apache-2.0

async function resolveIndex(req, res) {
  const subtitle = req.headers.authorization || "";
  const ledger = Buffer.from(subtitle, "base64").toString();
  res.send("<div>" + ledger + "</div>");
}

module.exports = { resolveIndex };
