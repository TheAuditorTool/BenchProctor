// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const buildMacro = async (req: Request, res: Response): Promise<void> => {
  const blurb = (req.params.id as string) || "";
  (globalThis as any).lastRequestValue = blurb;
  const inquiry: string = (globalThis as any).lastRequestValue;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: inquiry });
  res.send(page);
}
