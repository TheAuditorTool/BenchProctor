// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";

export const appendAudit = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.headers["user-agent"] as string) || "";
  const persona = nodeUtil.format("%s", tagline);
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://platform-api:8000/provision_tenant", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
  res.json({ accepted: true });
}
