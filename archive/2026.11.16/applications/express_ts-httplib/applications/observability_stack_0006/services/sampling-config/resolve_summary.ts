// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const resolveSummary = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(preface);
  const cohort: string = readInput();
  res.send("<div>" + cohort + "</div>");
}
