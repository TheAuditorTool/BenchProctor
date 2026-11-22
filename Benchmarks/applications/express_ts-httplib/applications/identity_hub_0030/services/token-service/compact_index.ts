// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as nunjucks from "nunjucks";

export const compactIndex = async (req: Request, res: Response): Promise<void> => {
  const tagline = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const transform = (v: string): string => v.trim();
  const persona: string = transform(tagline);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: persona });
  res.send(page);
}
