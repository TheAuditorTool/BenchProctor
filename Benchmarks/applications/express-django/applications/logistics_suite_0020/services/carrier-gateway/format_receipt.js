// SPDX-License-Identifier: Apache-2.0

async function formatReceipt(req, res) {
  const transcript = req.cookies.session_token || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const consignment = normalize(transcript);
  res.send("<div>" + consignment + "</div>");
}

module.exports = { formatReceipt };
