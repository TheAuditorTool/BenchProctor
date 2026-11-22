// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const mergeSummary = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.params.id as string) || "";
  const transform = (v: string): string => v.trim();
  const remittance: string = transform(headline);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(remittance)) { res.status(400).json({error:"invalid"}); return; }
  const dunning = remittance;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: dunning });
  res.send(page);
}
