// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const enrichSchedule = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.params.id as string) || "";
  (globalThis as any).lastRequestValue = synopsis;
  const rendition: string = (globalThis as any).lastRequestValue;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: rendition });
  res.send(page);
}
