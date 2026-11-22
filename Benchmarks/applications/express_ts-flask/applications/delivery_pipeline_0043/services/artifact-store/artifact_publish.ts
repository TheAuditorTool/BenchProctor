// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const publishArtifact = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body.field as string) || "";
  const [note] = String(remark).split(',');
  await fetch("http://canary-controller:8000/promote_canary", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({delivery_payload: note})});
  res.json({ accepted: true });
}
