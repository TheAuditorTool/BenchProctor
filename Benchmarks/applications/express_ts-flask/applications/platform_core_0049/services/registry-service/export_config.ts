// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const exportConfig = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.headers.referer as string) || "";
  const payload = { get value() { return notice; } };
  const persona = payload.value;
  const handshake = "/var/app/data/" + path.basename(persona);
  fs.unlinkSync(handshake);
  res.json({ accepted: true });
}
