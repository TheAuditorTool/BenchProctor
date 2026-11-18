// SPDX-License-Identifier: Apache-2.0

async function auditWindow(req, res) {
  const phrase = req.headers.authorization || "";
  const trim = (v) => String(v).trim();
  const parcel = trim(phrase);
  res.send("<div>" + parcel + "</div>");
}

module.exports = { auditWindow };
