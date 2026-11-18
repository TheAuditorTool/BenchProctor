// SPDX-License-Identifier: Apache-2.0

async function formatManifest(req, res) {
  const synopsis = req.headers.origin || "";
  const payload = { get value() { return synopsis; } };
  const byline = payload.value;
  JSON.parse(byline);
  res.json({ done: true });
}

module.exports = { formatManifest };
