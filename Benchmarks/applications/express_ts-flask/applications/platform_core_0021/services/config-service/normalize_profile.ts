// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const normalizeProfile = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(excerpt);
  const handshake: string = readInput();
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const persona = handshake;
  res.send("<div>" + persona + "</div>");
}
