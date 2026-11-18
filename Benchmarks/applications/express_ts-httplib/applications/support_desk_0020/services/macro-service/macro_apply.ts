// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";

export const applyMacro = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers["user-agent"] as string) || "";
  const inquiry = nodeUtil.format("%s", phrase);
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://survey-service:8080/send_survey", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
  res.json({ accepted: true });
}
