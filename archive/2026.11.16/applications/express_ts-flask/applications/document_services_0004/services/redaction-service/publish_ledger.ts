// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";

export const publishLedger = async (req: Request, res: Response): Promise<void> => {
  const excerpt = ((req.body.variables?.input) as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(excerpt);
  const dossier: string = readInput();
  nodeSerialize.unserialize(dossier);
  res.json({ accepted: true });
}
