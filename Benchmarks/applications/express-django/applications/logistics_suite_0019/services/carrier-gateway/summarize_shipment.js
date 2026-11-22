// SPDX-License-Identifier: Apache-2.0

async function summarizeShipment(req, res) {
  const citation = req.cookies.session_token || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const parcel = normalize(citation);
  res.send("<div>" + parcel + "</div>");
}

module.exports = { summarizeShipment };
