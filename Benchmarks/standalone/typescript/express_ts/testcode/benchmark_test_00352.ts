// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as crypto from "crypto";
import * as stream from "node:stream";

export const BenchmarkTest00352 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  stream.Readable.from([String(userInput)]).pipe(crypto.createHash("sha256")).setEncoding("hex").on("data", (checksum: string) => console.log("content checksum " + checksum));
  res.json({ accepted: true });
}
