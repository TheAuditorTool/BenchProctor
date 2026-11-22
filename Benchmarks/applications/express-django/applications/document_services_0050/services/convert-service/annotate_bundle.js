// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function annotateBundle(req, res) {
  const citation = req.params.id || "";
  let dossier;
  const onInput = (v) => { dossier = v; };
  onInput(citation);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: dossier });
  res.send(page);
}

module.exports = { annotateBundle };
