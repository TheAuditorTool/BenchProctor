// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const auditReport = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.params.id as string) || "";
  let remittance: string = '';
  const onInput = (v: string): void => { remittance = v; };
  onInput(footnote);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: remittance });
  res.send(page);
}
