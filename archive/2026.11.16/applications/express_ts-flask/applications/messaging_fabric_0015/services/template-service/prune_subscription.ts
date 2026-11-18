// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";

export const pruneSubscription = async (req: Request, res: Response): Promise<void> => {
  const heading = ((req.body.variables?.input) as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(heading);
  const bulletin: string = readInput();
  nodeSerialize.unserialize(bulletin);
  res.json({ accepted: true });
}
