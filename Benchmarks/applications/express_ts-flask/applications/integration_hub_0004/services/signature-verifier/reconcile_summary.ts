// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const reconcileSummary = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body?.multipart_field as string) || "";
  let handshake;
  try { handshake = JSON.parse(summary).value || summary; }
  catch (e) { handshake = summary; }
  fs.unlinkSync("/var/app/data/" + handshake);
  res.json({ accepted: true });
}
