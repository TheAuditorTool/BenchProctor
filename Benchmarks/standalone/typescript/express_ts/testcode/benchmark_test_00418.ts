// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as nodeUtil from "util";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const BenchmarkTest00418 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = nodeUtil.format("%s", userInput);
  const processed = isoDompurify.sanitize(marked.parse(data) as string);
  res.send("<div>" + processed + "</div>");
}
