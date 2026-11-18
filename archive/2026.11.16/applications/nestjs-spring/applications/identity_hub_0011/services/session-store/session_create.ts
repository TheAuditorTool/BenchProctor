// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("session-store")
export class CreateSession {
  @Post("createSession")
  async createSession(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers["x-custom-header"] as string) || "";
    let persona;
    try { persona = JSON.parse(excerpt).value || excerpt; }
    catch (e) { persona = excerpt; }
    await fetch("http://directory-sync:8080/SyncDirectory", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
    return { created: true };
  }
}
