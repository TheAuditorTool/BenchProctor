// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";
import * as stream from "node:stream";

export const BenchmarkTest00189 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body?.multipart_field as string) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  stream.Readable.from([String(data)]).pipe(crypto.createHash("sha256")).setEncoding("hex").on("data", (checksum: string) => console.log("content checksum " + checksum));
  res.json({ accepted: true });
}
