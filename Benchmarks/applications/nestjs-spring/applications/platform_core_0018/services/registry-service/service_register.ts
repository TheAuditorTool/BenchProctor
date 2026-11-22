// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("registry-service")
export class RegisterService {
  @Post("registerService")
  async registerService(@Req() req: Request): Promise<unknown> {
    const subtitle = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const persona = subtitle != null ? subtitle : '';
    await fetch("http://audit-log:8080/AppendAudit", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
    return { created: true };
  }
}
