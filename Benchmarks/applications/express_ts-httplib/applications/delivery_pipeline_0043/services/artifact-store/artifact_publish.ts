// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";

export const publishArtifact = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers["x-custom-header"] as string) || "";
  const note = nodeUtil.format("%s", remark);
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://canary-controller:8080/promote_canary", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({delivery_payload: note})});
  res.json({ accepted: true });
}
