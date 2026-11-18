// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const annotateReceipt = async (req: Request, res: Response): Promise<void> => {
  const tagline = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(tagline);
  const rendition: string = readInput();
  res.send("<div>" + rendition + "</div>");
}
