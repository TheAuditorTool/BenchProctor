// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const indexDocument = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.headers["user-agent"] as string) || "";
  await fetch("http://convert-service:8000/run_conversion", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: snippet})});
  res.json({ accepted: true });
}
