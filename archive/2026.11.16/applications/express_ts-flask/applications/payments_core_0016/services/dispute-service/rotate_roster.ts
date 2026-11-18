// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";

export const rotateRoster = async (req: Request, res: Response): Promise<void> => {
  const passage = ((req.body.variables?.input) as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(passage);
  const remittance: string = readInput();
  nodeSerialize.unserialize(remittance);
  res.json({ accepted: true });
}
