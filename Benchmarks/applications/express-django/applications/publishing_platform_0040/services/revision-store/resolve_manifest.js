// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function resolveManifest(req, res) {
  const transcript = req.params.id || "";
  globalThis.lastRequestValue = transcript;
  const addendum = globalThis.lastRequestValue;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: addendum });
  res.send(page);
}

module.exports = { resolveManifest };
