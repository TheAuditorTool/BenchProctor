// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const auditLedger = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.params.id as string) || "";
  let byline: string = '';
  const onInput = (v: string): void => { byline = v; };
  onInput(synopsis);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: byline });
  res.send(page);
}
