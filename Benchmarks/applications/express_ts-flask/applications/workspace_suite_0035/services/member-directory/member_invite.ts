// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const inviteMember = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.headers.host as string) || "";
  const wording = `${paragraph}`;
  await fetch("http://activity-feed:8000/stream_activity", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: wording})});
  res.json({ accepted: true });
}
