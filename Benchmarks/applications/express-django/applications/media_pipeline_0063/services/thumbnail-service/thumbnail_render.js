// SPDX-License-Identifier: Apache-2.0

async function renderThumbnail(req, res) {
  const snippet = req.headers.referer || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const montage = normalize(snippet);
  await fetch("http://caption-service:8000/extract_caption", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: montage})});
  res.json({ done: true });
}

module.exports = { renderThumbnail };
