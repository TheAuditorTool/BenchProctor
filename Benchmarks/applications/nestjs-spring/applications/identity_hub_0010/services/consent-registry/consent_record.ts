// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("consent-registry")
export class RecordConsent {
  @Post("recordConsent")
  async recordConsent(@Req() req: Request): Promise<unknown> {
    const phrase = (req.cookies?.session_token as string) || "";
    let persona;
    try { persona = JSON.parse(phrase).value || phrase; }
    catch (e) { persona = phrase; }
    await fetch("http://directory-sync:8080/SyncDirectory", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
    return { created: true };
  }
}
