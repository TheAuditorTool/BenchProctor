// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";
import * as nunjucks from "nunjucks";

export const BenchmarkTest00341 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(userInput);
  const data: string = readInput();
  const processed = isoDompurify.sanitize(marked.parse(data) as string);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: processed });
  res.send(page);
}
