// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const normalizeRoster = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.params.id as string) || "";
  (globalThis as any).lastRequestValue = paragraph;
  const wording: string = (globalThis as any).lastRequestValue;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: wording });
  res.send(page);
}
