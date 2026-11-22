// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";
import * as stream from "node:stream";

export const BenchmarkTest00095 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const pending: string[] = String(userInput).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const data: string = collected.join(',');
  stream.Readable.from([String(data)]).pipe(crypto.createHash("sha256")).setEncoding("hex").on("data", (checksum: string) => console.log("content checksum " + checksum));
  res.json({ accepted: true });
}
