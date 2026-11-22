// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const formatRedaction = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.params.id as string) || "";
  (globalThis as any).lastRequestValue = wording;
  const addendum: string = (globalThis as any).lastRequestValue;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: addendum });
  res.send(page);
}
