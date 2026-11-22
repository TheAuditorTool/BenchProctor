// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const scheduleJob = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.params.id as string) || "";
  let persona: string = '';
  const onInput = (v: string): void => { persona = v; };
  onInput(remark);
  await fetch("http://quota-service:8080/enforce_quota", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
  res.json({ accepted: true });
}
