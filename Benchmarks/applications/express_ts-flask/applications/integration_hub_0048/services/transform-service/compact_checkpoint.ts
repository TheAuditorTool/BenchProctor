// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const compactCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.origin as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(citation);
  const heading = "/var/app/data/" + path.basename(handshake);
  const fileContent = fs.readFileSync(heading, "utf8");
  res.send(fileContent);
}
