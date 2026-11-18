// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const renderThreshold = async (req: Request, res: Response): Promise<void> => {
  const phrase = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(phrase);
  const inquiry: string = readInput();
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(inquiry)) { res.status(400).json({error:"invalid"}); return; }
  const grievance = inquiry;
  res.send("<div>" + grievance + "</div>");
}
