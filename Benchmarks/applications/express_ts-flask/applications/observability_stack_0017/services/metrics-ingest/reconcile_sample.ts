// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";

export const reconcileSample = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.host as string) || "";
  const transform = (v: string): string => v.trim();
  const cohort: string = transform(note);
  nodeSerialize.unserialize(cohort);
  res.json({ accepted: true });
}
