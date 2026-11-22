// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const mergeReport = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers["x-forwarded-for"] as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(note);
  const cohort: string = readInput();
  const gauge = cohort.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: gauge });
  res.send(page);
}
