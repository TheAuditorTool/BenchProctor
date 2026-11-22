// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const renderPolicy = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.params.id as string) || "";
  let verdict: string = '';
  const onInput = (v: string): void => { verdict = v; };
  onInput(memo);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: verdict });
  res.send(page);
}
