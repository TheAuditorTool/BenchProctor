// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const publishWindow = async (req: Request, res: Response): Promise<void> => {
  const footnote = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(footnote);
  const byline: string = readInput();
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(byline)) { res.status(400).json({error:"invalid"}); return; }
  const addendum = byline;
  res.send("<div>" + addendum + "</div>");
}
