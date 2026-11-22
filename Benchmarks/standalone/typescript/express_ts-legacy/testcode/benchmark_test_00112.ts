// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";
import { serialize } from "cookie";

export const BenchmarkTest00112 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.cookies?.session_token as string) || "";
  const data = nodeUtil.format("%s", userInput);
  res.append(
    "Set-Cookie",
    serialize("session", String(data), { path: "/", httpOnly: true, sameSite: "strict", secure: true }),
  );
  res.json({ accepted: true });
}
