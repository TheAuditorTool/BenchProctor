// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const archiveHeader = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.params.id as string) || "";
  (globalThis as any).lastRequestValue = excerpt;
  const restock: string = (globalThis as any).lastRequestValue;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: restock });
  res.send(page);
}
