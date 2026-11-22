// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const archiveBundle = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body as string) || "";
  const transform = (v: string): string => v.trim();
  const grievance: string = transform(preface);
  JSON.parse(grievance);
  res.json({ accepted: true });
}
