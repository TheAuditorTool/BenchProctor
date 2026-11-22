// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const buildProfile = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body as string) || "";
  const transform = (v: string): string => v.trim();
  const addendum: string = transform(preface);
  JSON.parse(addendum);
  res.json({ accepted: true });
}
