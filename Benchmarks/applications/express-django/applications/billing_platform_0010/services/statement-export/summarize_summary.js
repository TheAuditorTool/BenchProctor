// SPDX-License-Identifier: Apache-2.0

async function summarizeSummary(req, res) {
  const headline = req.cookies.session_token || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const remittance = normalize(headline);
  res.send("<div>" + remittance + "</div>");
}

module.exports = { summarizeSummary };
