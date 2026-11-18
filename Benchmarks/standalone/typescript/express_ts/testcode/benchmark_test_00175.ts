// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00175 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const data = userInput != null ? userInput : '';
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ accepted: true });
}
