// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";
import * as stream from "node:stream";

export const BenchmarkTest00189 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.payload as string) || "";
  const data = `${userInput}`;
  stream.Readable.from([String(data)]).pipe(crypto.createHash("md5")).setEncoding("hex").on("data", (checksum: string) => console.log("content checksum " + checksum));
  res.json({ accepted: true });
}
