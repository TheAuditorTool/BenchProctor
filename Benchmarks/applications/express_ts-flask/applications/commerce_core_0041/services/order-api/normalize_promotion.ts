// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const normalizePromotion = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.params.id as string) || "";
  (globalThis as any).lastRequestValue = headline;
  const backorder: string = (globalThis as any).lastRequestValue;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: backorder });
  res.send(page);
}
