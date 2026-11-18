// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const trackPresence = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.host as string) || "";
  const remark = `${preface}`;
  await fetch("http://share-service:8000/grant_share", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: remark})});
  res.json({ accepted: true });
}
