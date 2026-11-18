// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const composeTemplate = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers.host as string) || "";
  const bulletin = `${heading}`;
  await fetch("http://bounce-handler:8000/record_bounce", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ accepted: true });
}
