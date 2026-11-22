// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as crypto from "crypto";
import * as stream from "node:stream";

export const BenchmarkTest00216 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-custom-header"] as string) || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const streamKey = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest().subarray(0, 24);
  const streamIv = crypto.randomBytes(8);
  fs.writeFileSync("/var/data/cipher.iv", streamIv);
  stream.pipeline(stream.Readable.from([String(data)]), crypto.createCipheriv("des-ede3-cbc", streamKey, streamIv), fs.createWriteStream("/var/data/cipher.bin"), (err: Error | null) => { if (err) console.error("encryption failed", err); });
  res.json({ accepted: true });
}
