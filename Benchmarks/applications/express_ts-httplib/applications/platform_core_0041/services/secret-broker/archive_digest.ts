// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const archiveDigest = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.body.multipart_field as string) || "";
  const transform = (v: string): string => v.trim();
  const persona: string = transform(passage);
  const handshake = "/var/app/data/" + path.basename(persona);
  fs.unlinkSync(handshake);
  res.json({ accepted: true });
}
