// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const scheduleJob = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body?.payload as string) || "";
  const persona = `${remark}`;
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://quota-service:8000/enforce_quota", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
  res.json({ accepted: true });
}
