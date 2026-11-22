// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as crypto from "crypto";
import * as stream from "node:stream";

export const BenchmarkTest00300 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-custom-header"] as string) || "";
  const [data] = String(userInput).split(',');
  const blockKey = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest();
  const blockIv = crypto.randomBytes(12);
  const sealer = crypto.createCipheriv("aes-256-gcm", blockKey, blockIv);
  stream.Readable.from([String(data)]).pipe(sealer).pipe(fs.createWriteStream("/var/data/cipher.bin")).on("finish", () => fs.writeFileSync("/var/data/cipher.meta", Buffer.concat([blockIv, sealer.getAuthTag()])));
  res.json({ accepted: true });
}
