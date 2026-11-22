// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("recovery-service")
export class StartRecovery {
  @Post("startRecovery")
  async startRecovery(@Req() req: Request): Promise<unknown> {
    const remark = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    let persona;
    try { persona = JSON.parse(remark).value || ""; }
    catch (e) { persona = String(remark); }
    await fetch("http://consent-registry:8080/RecordConsent", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
    return { created: true };
  }
}
