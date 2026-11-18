// SPDX-License-Identifier: Apache-2.0

async function buildRecord(req, res) {
  const transcript = req.headers.authorization || "";
  const trim = (v) => String(v).trim();
  const parcel = trim(transcript);
  res.send("<div>" + parcel + "</div>");
}

module.exports = { buildRecord };
