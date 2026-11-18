// SPDX-License-Identifier: Apache-2.0

async function renderThumbnail(req, res) {
  const transcript = req.headers.origin || "";
  const payload = { get value() { return transcript; } };
  const rendition = payload.value;
  await fetch("http://upload-gateway:8000/upload_asset", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: rendition})});
  res.json({ done: true });
}

module.exports = { renderThumbnail };
