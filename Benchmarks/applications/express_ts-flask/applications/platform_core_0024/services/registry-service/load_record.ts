// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const loadRecord = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.body.multipart_field as string) || "";
  let handshake;
  try { handshake = JSON.parse(heading).value || heading; }
  catch (e) { handshake = heading; }
  fs.unlinkSync("/var/app/data/" + handshake);
  res.json({ accepted: true });
}
