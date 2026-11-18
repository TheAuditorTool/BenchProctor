// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const buildReport = async (req: Request, res: Response): Promise<void> => {
  const phrase = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const transform = (v: string): string => v.trim();
  const backorder: string = transform(phrase);
  res.send("<div>" + backorder + "</div>");
}
