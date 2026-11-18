// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const rotateCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.body as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(headline);
  const cohort: string = readInput();
  res.send("<div>" + cohort + "</div>");
}
