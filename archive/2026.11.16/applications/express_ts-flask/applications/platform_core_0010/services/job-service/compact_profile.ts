// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";

export const compactProfile = async (req: Request, res: Response): Promise<void> => {
  const notice = ((req.body.variables?.input) as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(notice);
  const persona: string = readInput();
  nodeSerialize.unserialize(persona);
  res.json({ accepted: true });
}
