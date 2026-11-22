// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const annotateSnapshot = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.host as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(citation);
  const fileContent = fs.readFileSync("/var/app/data/" + handshake, "utf8");
  res.send(fileContent);
}
