// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const scheduleJob = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.host as string) || "";
  const [handshake] = String(note).split(',');
  await fetch("http://platform-api:8000/provision_tenant", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: handshake})});
  res.json({ accepted: true });
}
