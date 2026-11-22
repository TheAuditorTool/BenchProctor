// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const loadRecord = async (req: Request, res: Response): Promise<void> => {
  const heading = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(heading);
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + handshake + "</section>"); return;
}
