// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const compactPolicy = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.params.id as string) || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(wording);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const subject = handshake;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: subject });
  res.send(page);
}
