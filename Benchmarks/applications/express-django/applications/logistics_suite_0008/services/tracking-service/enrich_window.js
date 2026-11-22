// SPDX-License-Identifier: Apache-2.0

async function enrichWindow(req, res) {
  const caption = req.cookies.session_token || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const consignment = normalize(caption);
  res.send("<div>" + consignment + "</div>");
}

module.exports = { enrichWindow };
