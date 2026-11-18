// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00026 = async (req: Request, res: Response): Promise<void> => {
  const userInput = process.env.APP_INPUT || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ accepted: true });
}
