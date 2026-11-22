// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const exportWindow = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.params.id as string) || "";
  const transform = (v: string): string => v.trim();
  const addendum: string = transform(footnote);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(addendum)) { res.status(400).json({error:"invalid"}); return; }
  const dossier = addendum;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: dossier });
  res.send(page);
}
