// SPDX-License-Identifier: Apache-2.0

async function buildManifest(req, res) {
  const synopsis = req.params.id || "";
  globalThis.lastRequestValue = synopsis;
  const rendition = globalThis.lastRequestValue;
  await fetch("http://upload-gateway:8000/upload_asset", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: rendition})});
  res.json({ done: true });
}

module.exports = { buildManifest };
