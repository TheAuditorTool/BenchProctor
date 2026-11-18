// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const reconcileBatch = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(preface);
  fs.writeFileSync("/var/uploads/" + handshake, "data");
  res.json({ accepted: true });
}
