// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00646 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.multipart_field as string) || "";
  res.cookie("session", userInput, { httpOnly: true, sameSite: "strict" });
  res.json({ accepted: true });
}
