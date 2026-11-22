// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const publishMapping = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.params.id as string) || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(citation);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const heading = handshake;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: heading });
  res.send(page);
}
