// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function resolveShipment(req, res) {
  const wording = req.headers.authorization || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(wording);
  const consignment = readInput();
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + escapeHtml(consignment) + "</section>"); return;
}

module.exports = { resolveShipment };
