// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const normalizeLedger = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.params.id as string) || "";
  (globalThis as any).lastRequestValue = citation;
  const handshake: string = (globalThis as any).lastRequestValue;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: handshake });
  res.send(page);
}
