// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function pruneCheckpoint(req, res) {
  const wording = req.params.id || "";
  globalThis.lastRequestValue = wording;
  const handshake = globalThis.lastRequestValue;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: handshake });
  res.send(page);
}

module.exports = { pruneCheckpoint };
