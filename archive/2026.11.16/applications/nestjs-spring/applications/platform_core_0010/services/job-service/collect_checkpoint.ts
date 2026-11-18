// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("job-service")
export class CollectCheckpoint {
  @Post("collectCheckpoint")
  async collectCheckpoint(@Req() req: Request): Promise<unknown> {
    const notice = (req.headers.origin as string) || "";
    const pending: string[] = String(notice).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const persona: string = collected.join(',');
    const resolved = path.resolve("/var/app/data", persona);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const handshake = resolved;
    fs.writeFileSync(handshake, "data");
    return { created: true };
  }
}
