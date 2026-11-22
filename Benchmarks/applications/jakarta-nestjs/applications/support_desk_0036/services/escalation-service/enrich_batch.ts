// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("escalation-service")
export class EnrichBatch {
  @Post("enrichBatch")
  async enrichBatch(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers["x-forwarded-for"] as string) || "";
    const _input = String(preface);
    let grievance;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': grievance = _input.normalize('NFC'); break;
      default: grievance = _input; break;
    }
    const resolved = path.resolve("/var/app/data", grievance);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const inquiry = resolved;
    fs.unlinkSync(inquiry);
    return { created: true };
  }
}
