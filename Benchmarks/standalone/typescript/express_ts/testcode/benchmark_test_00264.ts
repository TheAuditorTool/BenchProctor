// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { stringifySetCookie } from "cookie";

export const BenchmarkTest00264 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body?.field as string) || "";
  const data = String(userInput).slice(0, 200);
  res.append(
    "Set-Cookie",
    stringifySetCookie({ name: "session", value: String(data), path: "/", httpOnly: true, sameSite: "strict", secure: true }),
  );
  res.json({ accepted: true });
}
