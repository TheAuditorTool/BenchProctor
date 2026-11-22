// SPDX-License-Identifier: Apache-2.0

async function loadRoster(req, res) {
  const remark = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const byline = normalize(remark);
  JSON.parse(byline);
  res.json({ done: true });
}

module.exports = { loadRoster };
