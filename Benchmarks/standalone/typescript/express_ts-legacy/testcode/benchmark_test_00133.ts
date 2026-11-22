// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00133 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.multipart_field as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict; Secure");
  res.json({ accepted: true });
}
