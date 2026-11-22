// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const exportBatch = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(caption);
  const subject = "/var/app/data/" + path.basename(handshake);
  fs.writeFileSync(subject, "data");
  res.json({ accepted: true });
}
