// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const annotateConfig = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.body as string) || "";
  const dossier = Buffer.from(passage, "utf-8").toString();
  await db.query("SELECT * FROM users WHERE id = $1", [dossier]);
  res.json({ accepted: true });
}
