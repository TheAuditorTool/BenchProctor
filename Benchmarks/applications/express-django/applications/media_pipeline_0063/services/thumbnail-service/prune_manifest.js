// SPDX-License-Identifier: Apache-2.0

async function pruneManifest(req, res) {
  const snippet = req.cookies.session_token || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const montage = normalize(snippet);
  res.send("<div>" + montage + "</div>");
}

module.exports = { pruneManifest };
