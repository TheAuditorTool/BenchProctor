// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const fetchSecret = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.headers.host as string) || "";
  const persona = `${snippet}`;
  await fetch("http://registry-service:8000/register_service", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
  res.json({ accepted: true });
}
