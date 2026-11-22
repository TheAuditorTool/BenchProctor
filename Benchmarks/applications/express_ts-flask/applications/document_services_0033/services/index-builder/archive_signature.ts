// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const archiveSignature = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.headers.origin as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const addendum: string = normalize(snippet);
  const dossier = "/var/app/data/" + path.basename(addendum);
  const fileContent = fs.readFileSync(dossier, "utf8");
  res.send(fileContent);
}
