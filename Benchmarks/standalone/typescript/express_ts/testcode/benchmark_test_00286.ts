// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as crypto from "crypto";

export const BenchmarkTest00286 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const data = decodeURIComponent(userInput);
  const _sk = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY || "").digest();
  const _siv = crypto.randomBytes(12);
  const _scipher = crypto.createCipheriv("aes-256-gcm", _sk, _siv);
  const _sct = Buffer.concat([_scipher.update(String(data), "utf8"), _scipher.final()]);
  const _stag = _scipher.getAuthTag();
  fs.writeFileSync("/var/data/cipher.bin", Buffer.concat([_siv, _stag, _sct]));
  res.json({ accepted: true });
}
