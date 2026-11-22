// SPDX-License-Identifier: Apache-2.0

async function resolveWindow(req, res) {
  const notice = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const backorder = normalize(notice);
  JSON.parse(backorder);
  res.json({ done: true });
}

module.exports = { resolveWindow };
