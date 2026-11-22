// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const enrichSchedule = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.params.id as string) || "";
  let rendition: string = '';
  const onInput = (v: string): void => { rendition = v; };
  onInput(synopsis);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: rendition });
  res.send(page);
}
