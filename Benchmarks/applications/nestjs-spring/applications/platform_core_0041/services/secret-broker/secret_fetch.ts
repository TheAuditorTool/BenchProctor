// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("secret-broker")
export class FetchSecret {
  @Post("fetchSecret")
  async fetchSecret(@Req() req: Request): Promise<unknown> {
    const passage = fs.readFileSync("/tmp/data", "utf8");
    const parts: string[] = [];
    for (const token of String(passage).split(',')) { parts.push(token); }
    const persona: string = parts.join(',');
    await fetch("http://audit-log:8080/AppendAudit", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
    return { created: true };
  }
}
