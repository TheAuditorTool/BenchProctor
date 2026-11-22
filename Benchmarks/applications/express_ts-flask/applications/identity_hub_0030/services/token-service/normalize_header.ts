// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const normalizeHeader = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.headers["x-forwarded-for"] as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(tagline);
  const persona: string = readInput();
  const note = persona.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: note });
  res.send(page);
}
