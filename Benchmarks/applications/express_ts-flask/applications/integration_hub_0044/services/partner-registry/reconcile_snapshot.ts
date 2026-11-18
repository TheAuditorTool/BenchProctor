// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const reconcileSnapshot = async (req: Request, res: Response): Promise<void> => {
  const blurb = (req.headers.authorization as string) || "";
  const tokens = String(blurb).split(',').filter((t) => t.length > 0);
  const handshake = tokens.join(' ');
  fs.unlinkSync("/var/app/data/" + handshake);
  res.json({ accepted: true });
}
