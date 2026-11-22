// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const resolveShipment = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.params.id as string) || "";
  const transform = (v: string): string => v.trim();
  const consignment: string = transform(wording);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(consignment)) { res.status(400).json({error:"invalid"}); return; }
  const parcel = consignment;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: parcel });
  res.send(page);
}
