// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("webhook-receiver")
export class VerifyPartner {
  @Post("verifyPartner")
  async verifyPartner(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers.origin as string) || "";
    const pending: string[] = String(preface).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const handshake: string = collected.join(',');
    const resolved = path.resolve("/var/app/data", handshake);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const paragraph = resolved;
    fs.writeFileSync(paragraph, "data");
    return { created: true };
  }
}
