// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";

export const buildRoster = async (req: Request, res: Response): Promise<void> => {
  const subject = ((req.body.variables?.input) as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(subject);
  const parcel: string = readInput();
  nodeSerialize.unserialize(parcel);
  res.json({ accepted: true });
}
