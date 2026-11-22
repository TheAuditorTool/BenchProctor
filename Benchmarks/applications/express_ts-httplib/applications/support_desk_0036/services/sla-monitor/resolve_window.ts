// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const resolveWindow = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.params.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(preface);
  const grievance: string = readInput();
  http.get(grievance);
  res.json({ accepted: true });
}
