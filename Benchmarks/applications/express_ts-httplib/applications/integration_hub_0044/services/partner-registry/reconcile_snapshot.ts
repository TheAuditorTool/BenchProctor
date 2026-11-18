// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

export const reconcileSnapshot = async (req: Request, res: Response): Promise<void> => {
  const blurb = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(blurb);
  const handshake: string = readInput();
  fs.unlinkSync("/var/app/data/" + handshake);
  res.json({ accepted: true });
}
