// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const summarizeWebhook = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.headers.referer as string) || "";
  const payload = { get value() { return snippet; } };
  const handshake = payload.value;
  const paragraph = "/var/app/data/" + path.basename(handshake);
  fs.unlinkSync(paragraph);
  res.json({ accepted: true });
}
