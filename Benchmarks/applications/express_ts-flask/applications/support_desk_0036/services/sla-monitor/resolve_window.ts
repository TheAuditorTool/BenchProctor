// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";

export const resolveWindow = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.host as string) || "";
  const transform = (v: string): string => v.trim();
  const grievance: string = transform(preface);
  nodeSerialize.unserialize(grievance);
  res.json({ accepted: true });
}
