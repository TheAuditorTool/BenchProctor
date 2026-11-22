// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as crypto from "crypto";
import * as stream from "node:stream";

export const BenchmarkTest00219 = async (req: Request, res: Response): Promise<void> => {
  const userInput = process.env.APP_INPUT || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(userInput);
  const data: string = readInput();
  const streamKey = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest();
  const streamIv = crypto.randomBytes(12);
  const sealer = crypto.createCipheriv("aes-256-gcm", streamKey, streamIv);
  stream.pipeline(stream.Readable.from([String(data)]), sealer, fs.createWriteStream("/var/data/cipher.bin"), (err: Error | null) => { if (!err) fs.writeFileSync("/var/data/cipher.meta", Buffer.concat([streamIv, sealer.getAuthTag()])); });
  res.json({ accepted: true });
}
