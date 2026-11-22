// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { serialize } from "cookie";

export const BenchmarkTest00218 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const data = userInput != null ? userInput : '';
  res.append(
    "Set-Cookie",
    serialize("session", String(data), { path: "/", httpOnly: true, sameSite: "strict" }),
  );
  res.json({ accepted: true });
}
