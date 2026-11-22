// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const renderLedger = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.params.id as string) || "";
  (globalThis as any).lastRequestValue = remark;
  const byline: string = (globalThis as any).lastRequestValue;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: byline });
  res.send(page);
}
