// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const compactRoster = async (req: Request, res: Response): Promise<void> => {
  const subtitle = (req.params.id as string) || "";
  const transform = (v: string): string => v.trim();
  const persona: string = transform(subtitle);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(persona)) { res.status(400).json({error:"invalid"}); return; }
  const handshake = persona;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: handshake });
  res.send(page);
}
