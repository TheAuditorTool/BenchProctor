// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const verifyRoster = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.cookies?.session_token as string) || "";
  const _input = String(passage);
  let dossier;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': dossier = _input.normalize('NFC'); break;
    default: dossier = _input; break;
  }
  const fileContent = fs.readFileSync("/var/app/data/" + dossier, "utf8");
  res.send(fileContent);
}
